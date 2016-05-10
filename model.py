"""Models and database functions for Climbing Project"""

from flask_sqlalchemy import SQLAlchemy 

# This is the connection to the PostgreSQL database;
db= SQLAlchemy()

#################################
#Model definitions

class User(db.Model):
    """User of Climbing website"""
    #TODO

    #add table creation

    #add column creation

    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Location(db.Model):
    """Climbing Location"""
    #TODO

    #add table creation

    #add column creation


    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Location_rating(db.Model):
    """Location ratings"""
    #TODO
    
    #add table creation

    #add column creation

    def __repr__(self):
        """Provide helpful representation when printed."""
    pass
    
class Location_comment(db.Model):
    """Location comments"""
    #TODO

    #add table creation

    #add column creation
    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Route(db.Model):
    """Climbing routes"""
    #TODO
    
    #add table creation

    #add column creation
    
    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Route_rating(db.Model):
    """Route ratings"""
    #TODO
    
    #add table creation

    #add column creation

    def __repr__(self):
        """Provide helpful representation when printed."""
    pass

class Route_comment(db.Model):
    """Route comments"""
    #TODO
    
    #add table creation

    #add column creation
    
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



