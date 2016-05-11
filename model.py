"""Models and database functions for Climbing Project"""

from flask_sqlalchemy import SQLAlchemy 

# This is the connection to the PostgreSQL database;
db= SQLAlchemy()

#################################
#Model definitions

class User(db.Model):
    """User of Climbing website"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)


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
    directions = db.Column()#TODO
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    location_description #TODO
    


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Location: location_id=%s location_name=%s>" % (self.location_id,
                                                            self.location_name)
    

class Location_rating(db.Model):
    """Location ratings"""
    #TODO
    __tablename__ = 'location_ratings'
    
    location_rating_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    location_rating = db.Column(db.Integer, nullable=False)
    

    #TODO RELATIONSHIPS

    def __repr__(self):
        """Provide helpful representation when printed."""
        #how do i make this look better?
        return "<Location Rating: loc_rate_id=%s user_id=%s loc_id=%s loc_rate=%s>" % ( self.location_rating_id,
                                                                                        self.user_id,
                                                                                        self.location_id,
                                                                                        self.location_rating)
    
class Location_comment(db.Model):
    """Location comments"""
    #TODO
    __tablename__ = 'location_comments'
    #add table creation
    
    location_comment_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    location_comment 
    location_datetime

    #TODO RELATIONSHIPS
    
    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ( "<Location Comment: location_comment_id=%s user_id=%s>" % 
                (self.location_comment_id, self.user_id) )
    

class Route(db.Model):
    """Climbing routes"""
    #TODO
    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    route_name = db.Column(db.String(200), nullable=False)
    difficulty_rate = db.Column(db.String(5), nullable=True)
    route_description
  
    #TODO RELATIONSHIPS
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Routes: route_id=%s location_id=%s route_name=%s >" % 
                (self.route_id, location_id, route_name) )
    

class Route_rating(db.Model):
    """Route ratings"""
    #TODO
    __tablename__ = 'route_ratings'
    
    route_rating_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    route_rating = db.Column(db.Integer, nullable=True)
    route_difficulty_rate 

    #TODO RELATIONSHIPS

    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Route_comment(db.Model):
    """Route comments"""
    #TODO
    route_comment_id
    route_id
    user_id
    route_comment
    route_datetime
    
    #TODO RELATIONSHIPS
    
    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Images(db.Model):
    """Images uploaded from users"""
    #TODO AFTER FIRST SPRINT
    #add table creation

    #add column creation
    def __repr__(self):
        """Provide helpful representation when printed."""
    pass 


#################################
#Helper functions



