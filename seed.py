"""Utility file to seed boulders database from data_seed_files/"""
import csv

from model import Location ,connect_to_db, db
# Sub_location, Boulder, Route
from server import app


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

            # print parent_name
            # print name
            # print lat_long
            # print desc
            # print directions
            # print sub_locations
            # lat, lon = lat_long.split(', ')
            # print lat
            # print lon

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
    # open file
    # with open('data_seed_files/sub_locations.csv', 'r,') as csvfile:
    
    #     #checks to see if the file has a header
    #     has_header = csv.Sniffer().has_header(csvfile.read(1024))
    #     #resets the file back to the start
    #     csvfile.seek(0)

    #     # read in file
    #     my_file = csv.reader(csvfile, delimiter=',')
    #     #skips the header
    #     if has_header:
    #         next(my_file) #skip header row
    # # loop through the file
    #     for row in my_file:
    
    #use flask-sqlalchemy to query the db


    

    # unpack each row

    # query the db to get the location_id of a matching location name

    # create a new sub_location object

    # add it to db

    # commit the db when done.

# def load_boulders():
#     """Load boulders from boulders.csv"""

    # open file

    # read in file

    # loop through the file

    # unpack each row

    # query the db to get the sub_location_id of a matching location name
    
    # if yes get the sub_location_id and the sub_locations location_id

        # create a new boulder object

    # if there is no matching sub_location, query the db for a matching location
    #name and retreive the location_id

        # create a new boulder object 

    # add it to db

    # commit the db when done.


# def load_routes():
#     """Load routes from bouldering_routes2.csv, bouldering_routes_1.csv into db"""

    # open file

    # read in file

    # loop through the file

    # unpack each row

    # query the db to get the boulder_id of a matching boulder name

    # create a new route object

    # add it to db

    # commit the db when done.


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_locations()


