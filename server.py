""" Put something here"""
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, session, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Location, Sub_location, Boulder, Route
import hashing 

app = Flask(__name__)

app.secret_key = "something-secret"

app.jinja_env.undefined = StrictUndefined


#############
#The routes

@app.route('/')
def index():
    """Homepage"""

    return render_template('homepage.html')


@app.route('/register', methods=['GET'])
def register_form():
    """displays the user register"""
    
    #renders a user sign up form
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_process():
    """handles the user register form"""
    
    #get form variables
    email = request.form.get('email')
    password = request.form.get('pwd')
    username = request.form.get('username')

    hashed_password = hashing.hash_password(password)
    print hashed_password


    #check if username in db
    user = User.query.filter( (User.username == username) | (User.email == email) ).first()

    # if user is empty add user to db
    if not user:
        #add user to db
        new_user = User(email=email, username=username, password=hashed_password)
        flash("Welcome %s."  % (username))
        db.session.add(new_user)
        db.session.commit()

        created_user = User.query.filter_by(username=username).first()

        #create the key value pair in the session(= magic dictionary)
        #(flask's session)
        session['user_id'] = created_user.user_id
        
        # renders a user page
        return render_template('user_page.html')
    else:
        if user.email == email:
            flash("%s email already has an account."  % (email))
            return redirect("/")
        else:
            flash("%s username is already taken. Choose something else." % (username)) 
            return redirect("/")

    

@app.route('/login', methods=['POST'])
def login_user():
    """Handles user login"""

    # get username and password from form
    password = request.form.get('pwd')
    username = request.form.get('username')

    # find matching username in db
    user = User.query.filter_by(username=username).first()

    # no username match, got back to homepage
    if not user:
        flash("No username registered with the name %s" % (username))
        return redirect('/')

    # if user object is there get hashed pwd compare w/ entered pwd
    else:
        if hashing.check_password(user.password, password):
            #if a match send to user page
            flash("Sucessfully logged in.")
            
            #create the key value pair in the session(= magic dictionary)
            #(flask's session)
            session['user_id'] = user.user_id

            return render_template('user_page.html')
        # no match got back to homepage, Do Not Collect 200.
        else:
            flash("Incorrect password entered")
            return redirect('/')

    

@app.route('/logout')
def logout_user():
    """Logs out user and flashes a logout message"""

    # deletes the key and value in the session dictionary
    del session['user_id']
    flash("You have been logged out.")

    return redirect('/')


@app.route('/locations')
def display_location():
    """Display location list page"""

    #lists the location's routes as links
    locations = Location.query.order_by('location_name').all()
    return render_template("location.html", locations=locations)

@app.route("/locations/<int:location_id>", methods=['GET'])
def location_detail(location_id):
    """Show info about a location."""

    #get the location object
    location = Location.query.get(location_id)
    #find all sublocations that have the location as a parent
    sub_locations = Sub_location.query.filter_by(location_id=location_id).all()

    #find boulders that match the location_id, but dont have a
    #assoicated sub_location_id
    boulders = Boulder.query.filter((Boulder.location_id==location_id) & (Boulder.sub_location_id==None)).all()
        
    return render_template("location_detail.html", location=location,
                                                 sub_locations=sub_locations,
                                                 boulders=boulders )

@app.route("/sub_locations/<int:sub_location_id>", methods=['GET'])
def sub_location_detail(sub_location_id):
    """Shows a sub location details page"""
    #find the sublocation object
    sub = Sub_location.query.get(sub_location_id)
    #find the boulders that have the sublocation as a parent
    boulders = Boulder.query.filter_by(sub_location_id=sub_location_id).all()

    return render_template("sub_location.html", sub_location=sub,
                                                boulders=boulders)
    
 


@app.route("/boulders/<int:boulder_id>", methods=['GET'])
def boulder_detail(boulder_id):
    #find the Boulder object
    boulder = Boulder.query.get(boulder_id)
    #find all routes connected to that boulder
    routes = Route.query.filter_by(boulder_id=boulder_id).all()

    return render_template("boulders.html", boulder=boulder,
                                            routes=routes)

@app.route('/route/<int:route_id>', methods=['GET'])
def display_route(route_id):
    """Display route details page"""
    #get the route object
    route = Route.query.get(route_id)
    #find other routes that are on the same boulder
    near_routes = Route.query.filter((Route.boulder_id==route.boulder_id) & 
                                    (Route.route_name != route.route_name)).all()
    #find near_by boulders
    boulder = Boulder.query.filter_by(boulder_id=route.boulder_id).first()
    print boulder
    if boulder.sub_location_id:
        boulders = Boulder.query.filter_by(sub_location_id=boulder.sub_location_id).all()
    else:
        boulders = Boulder.query.filter_by(location_id=boulder.location_id).all()
    return render_template("route.html", route=route,
                                        near_routes=near_routes,
                                        boulders=boulders)

@app.route('/search.json', methods=['GET'])
def search():
    """searching for locations"""
    search_term = request.args.get('term')

    locations = Location.query.filter(Location.location_name.ilike('%'+search_term+'%')).all()
    sub_locations = Sub_location.query.filter(Sub_location.sub_location_name.ilike('%'+search_term+'%')).all()
    boulders = Boulder.query.filter(Boulder.boulder_name.ilike('%'+search_term+'%')).all()
    routes = Route.query.filter(Route.route_name.ilike('%'+search_term+'%')).all()

    results = []

    for location in locations:
        temp_dict = {}
        temp_dict["name"] = location.location_name
        temp_dict["lat"] = location.latitude
        temp_dict["lon"] = location.longitude
        temp_dict["id"] = location.location_id
        temp_dict["route"] = "/locations/"

        results.append(temp_dict)

    for sub in sub_locations:
        temp_dict = {}
        temp_dict["name"] = sub.sub_location_name
        temp_dict["lat"] = sub.sub_latitude
        temp_dict["lon"] = sub.sub_longitude
        temp_dict["id"] = sub.sub_location_id
        temp_dict["route"] = "/sub_locations/"

        results.append(temp_dict)

    for boulder in boulders:
        temp_dict = {}
        temp_dict["name"] = boulder.boulder_name
        temp_dict["lat"] = boulder.boulder_latitude
        temp_dict["lon"] = boulder.boulder_longitude
        temp_dict["id"] = boulder.boulder_id
        temp_dict["route"] = "/boulders/"

        results.append(temp_dict)

    for route in routes:
        temp_dict = {}
        temp_dict["name"] = route.route_name
        temp_dict["lat"] = ""
        temp_dict["lon"] = ""
        temp_dict["id"] = route.route_id
        temp_dict["route"] = "/route/"

        results.append(temp_dict)

    return jsonify({'data':results})






@app.route('/add_location')
def add_location():
    """Adds a location to the db"""

    #must be logged in 

    pass

@app.route('/add_route')
def add_route():
    """adds a route to a location in the db"""

    #must be logged in
    #must have a location

    pass





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
