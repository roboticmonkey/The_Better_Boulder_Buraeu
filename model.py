"""Models and database functions for Climbing Project"""

# from flask_sqlalchemy import SQLAlchemy 


# This is the connection to the PostgreSQL database;
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///boulders'
db = SQLAlchemy()





#################################
#Model definitions

class User(db.Model):
    """User of Climbing website"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<User: user_id=%s username=%s email=%s>" % (self.user_id,
                                                        self.username,
                                                        self.email)
    

class Location(db.Model):
    """Climbing Location"""
    
    __tablename__ = 'locations'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_name = db.Column(db.String(100), nullable=False)
    directions = db.Column(db.Text, nullable=True)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    location_description = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Location: location_id=%s location_name=%s>" % (self.location_id,
                                                            self.location_name)
    

class Location_rating(db.Model):
    """Location ratings"""
    
    __tablename__ = 'location_ratings'
    
    location_rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_rating = db.Column(db.Integer, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    #RELATIONSHIPS
    location = db.relationship('Location', backref='Location_rating')
    user = db.relationship('User', backref='Location_rating')

    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ("<Location Rating: loc_rate_id=%s user_id=%s loc_id=%s loc_rate=%s>" 
                % ( self.location_rating_id, self.user_id,
                    self.location_id, self.location_rating) )
 

class Location_comment(db.Model):
    """Location comments"""
    
    __tablename__ = 'location_comments'
    
    
    location_comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_comment = db.Column(db.Text, nullable=False)
    location_datetime = db.Column(db.DateTime, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    #RELATIONSHIPS
    location = db.relationship('Location', backref='Location_comment')
    user = db.relationship('User', backref='Location_comment')
    
    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ( "<Location Comment: location_comment_id=%s user_id=%s>" % 
                (self.location_comment_id, self.user_id) )
    

class Route(db.Model):
    """Climbing routes"""
    
    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_name = db.Column(db.String(200), nullable=False)
    difficulty_rate = db.Column(db.String(5), nullable=True)
    route_description = db.Column(db.Text, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
  
    #RELATIONSHIPS
    location = db.relationship('Location', backref='Route')
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Routes: route_id=%s location_id=%s route_name=%s >" % 
                (self.route_id, location_id, route_name) )
    

class Route_rating(db.Model):
    """Route ratings"""
    
    __tablename__ = 'route_ratings'
    
    route_rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_rating = db.Column(db.Integer, nullable=True)
    route_difficulty_rate = db.Column(db.Integer, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))

    #RELATIONSHIPS
    user = db.relationship('User', backref='Route_rating')
    route = db.relationship('Route', backref='Route_rating')


    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ("<Route Rating: id=%s route_id=%s route_rating=%s difficulty_rate=%s>"
                % (self.route_rating_id, route_id, route_rating, route_difficulty_rate))


class Route_comment(db.Model):
    """Route comments"""
    
    __tablename__ = 'route_comments'

    route_comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_comment = db.Column(db.Text, nullable=False)
    route_datetime = db.Column(db.DateTime, nullable=False)

    route_id  = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    #RELATIONSHIPS
    user = db.relationship('User', backref='Route_comment')
    route = db.relationship('Route', backref='Route_comment')
    
    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Route Comment: id=%s route_id=%s>" % (route_comment_id, route_id)


# class Images(db.Model):
#     """Images uploaded from users"""
#     #TODO AFTER FIRST SPRINT
#     #add table creation

#     #add column creation
#     def __repr__(self):
#         """Provide helpful representation when printed."""
#     pass 


#################################
#Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///boulders'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."



