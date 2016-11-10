"""Utility file to seed boulders database from data_seed_files/"""
import csv

from model import Location, Sub_location,Boulder, Route, connect_to_db, db
 
from server import app

import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


def load_locations():
    """Load locations from top_locations.csv into boulders db"""

    # open file
    with open('data_seed_files/top_locations.csv', 'r,') as csvfile:
    
        #checks to see if the file has a header
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        #resets the file back to the start
        csvfile.seek(0)

        # read in file
        my_file = csv.reader(csvfile, delimiter=',')
        #skips the header
        if has_header:
            next(my_file) #skip header row
    # loop through the file
        for row in my_file:
    # unpack each row
            parent_name, name, lat_long, desc, directions, sub_locations = row

            lat, lon = lat_long.split(', ')

            # create a new location object
            location = Location(location_name=name,
                                location_directions=directions,
                                location_description=desc,
                                latitude=lat,
                                longitude=lon)

            # add it to db
            db.session.add(location)           

    # commit the db when done.
    db.session.commit()



def load_sub_locations():
    """Load sub_locations from sub_locations.csv into boulders db"""

    # open file
    with open('data_seed_files/sub_locations.csv', 'r,') as csvfile:
        #checks to see if the file has a header
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        #resets the file back to the start
        csvfile.seek(0)

        # read in file
        my_file = csv.reader(csvfile, delimiter=',')
        #skips the header
        if has_header:
            next(my_file) #skip header row
    # loop through the file
        for row in my_file:
            # unpack each row
            parent_name, name, lat_long, desc, directions, sub_loc = row


            if lat_long:

                lat, lon = lat_long.split(', ')
            else:
                lat = ""
                lon = ""
      

            #use flask-sqlalchemy to query the db
            # query the db to get the location_id of a matching location name
            parent = Location.query.filter_by(location_name=parent_name).first()
 
            
            parent_id = parent.location_id


    # create a new sub_location object
            sub = Sub_location(sub_location_name=name, 
                                sub_location_directions=directions,
                                sub_location_description=desc,
                                sub_latitude=lat,
                                sub_longitude=lon,
                                location_id=parent_id)
            # add it to db
            db.session.add(sub)

        # commit the db when done.
        db.session.commit()

    

def load_boulders():
    """Load boulders from boulders.csv"""

    # open file
    with open('data_seed_files/boulders.csv', 'r,') as csvfile:
        #checks to see if the file has a header
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        #resets the file back to the start
        csvfile.seek(0)

        # read in file
        my_file = csv.reader(csvfile, delimiter=',')
        #skips the header
        if has_header:
            next(my_file) #skip header row
    # loop through the file
        for row in my_file:
            # unpack each row
            parent_name, name, lat_long, desc, directions, routes = row
            parent_name = parent_name.strip()


            #checks if lat_long is empty string
            if lat_long:

                lat, lon = lat_long.split(', ')
            else:
                lat = ""
                lon = ""

    # query the db to get the sub_location_id of a matching location name
            parent = Sub_location.query.filter_by(sub_location_name=parent_name).first()

            # print "sub location look", parent
            # if yes get the sub_location_id and the sub_locations location_id
            if parent:
                parent_id = parent.sub_location_id
                g_parent_id = parent.location_id
                # print "parent: %i g_parent: %i" % (parent_id, g_parent_id)

                #     create a new boulder object
                rock = Boulder(boulder_name=name,
                                boulder_description=desc,
                                boulder_directions=directions,
                                boulder_latitude=lat,
                                boulder_longitude=lon,
                                location_id=g_parent_id,
                                sub_location_id=parent_id)

                #add to db
                db.session.add(rock)
 # if there is no matching sub_location, query the db for a matching location
    # name and retreive the location_id
            if not parent:
                parent = Location.query.filter_by(location_name=parent_name).first()
                
                parent_id = parent.location_id
                
                
                #     create a new boulder object
                rock = Boulder(boulder_name=name,
                                boulder_description=desc,
                                boulder_directions=directions,
                                boulder_latitude=lat,
                                boulder_longitude=lon,
                                location_id=parent_id)

                #add to db
                db.session.add(rock)

    # commit the db when done.
            db.session.commit()


def load_routes(the_file):
    """Load routes from bouldering_routes2.csv, bouldering_routes_1.csv into db"""
    
    # open file
    with open(the_file, 'r,') as csvfile:
        #checks to see if the file has a header
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        #resets the file back to the start
        csvfile.seek(0)

        # read in file
        my_file = csv.reader(csvfile, delimiter=',')
        #skips the header
        if has_header:
            next(my_file) #skip header row
    # loop through the file
        for row in my_file:
            # unpack each row
            parent_name, name, difficulty, desc, directions, protection = row
            parent_name = parent_name.strip()
           

    # query the db to get the boulder_id of a matching boulder name
            parent = Boulder.query.filter_by(boulder_name=parent_name).first()
            
            parent_id=parent.boulder_id
            

    # create a new route object
            route = Route(route_name=name,
                            difficulty_rate=difficulty,
                            route_directions=directions,
                            route_description=desc,
                            route_protection=protection,
                            boulder_id=parent_id)

    # add it to db
            db.session.add(route)

    # commit the db when done.
        db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_locations()
    load_sub_locations()
    load_boulders()
    load_routes('data_seed_files/bouldering_routes_1.csv')
    load_routes('data_seed_files/bouldering_routes2.csv')


