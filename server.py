""" Put something here"""

from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db

app = Flask(__name__)

app.secret_key = "something-secret"



#############
#The routes

@app.route('/')
def index():
    """Homepage"""

    return render_template('homepage.html')




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
