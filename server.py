""" Put something here"""
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, session

from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User
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

    new_user = User(email=email, username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    #renders a user page
    return render_template('user_page.html')

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
        return redirect('/')

    # if user object is there get hashed pwd compare w/ entered pwd
    else:
        if hashing.check_password(user.password, password):
            #if a match send to user page
            return render_template('user_page.html')
        # no match got back to homepage, Do Not Collect 200.
        else:
            return redirect('/')

    

@app.route('/logout')
def logout_user():
    """ Logs out user"""

    pass


@app.route('/location')
def display_location():
    """Display location info page"""

    #lists the location's routes as links

    pass

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
