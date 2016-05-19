""" Put something here"""
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, session, flash

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

    location = Location.query.get(location_id)

    sub_locations = Sub_location.query.filter_by(location_id=location_id).all()

    boulders=None
    if not sub_locations:
        # return render_template("location_detail.html", location=location,
                                                     # sub_locations=sub_locations)
    # else:
        boulders = Boulder.query.filter_by(location_id=location_id).all()
        
    return render_template("location_detail.html", location=location,
                                                    
                                                 sub_locations=sub_locations,
                                                 boulders=boulders )

    
 

@app.route('/route')
def display_route():
    """Display route info page"""

    pass

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
