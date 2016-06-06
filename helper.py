"""Helper functions for Server.py"""

from model import Boulder, Route


def convert_sublocations_dict(sub_locations):
    """Takes a list of sub location objects and returns
        a list of dictionaries for converting to json"""

    results = []

    # print "\n this is the start of helper function: multiple"
    # print sub_locations, " is of type: ", type(sub_locations)

    for sub in sub_locations:
        # print sub
        sub_dict = convert_sublocation_dict(sub)

        results.append(sub_dict)
    # print "\n these are the results from helper function: multiple"
    # print results

    return results

def convert_sublocation_dict(sub_location):
    """Takes a sub location object and returns
        a dictionary for converting to json"""

    sub = sub_location
    
    results = []

    # print "\n this is the start of helper function: single"
    # print sub
    # print type(sub)

    
    temp_dict = {}
    temp_dict["name"] = sub.sub_location_name
    temp_dict["lat"] = sub.sub_latitude
    temp_dict["lon"] = sub.sub_longitude
    temp_dict["id"] = sub.sub_location_id
    temp_dict["route"] = "/sub_locations/"

    
    results = temp_dict
    # print "\n these are the results from helper function: single"
    # print results

    return results

def convert_boulders_dict(boulders):
    """Takes a list of boulder objects and returns
        a list of dictionaries for converting to json"""

    results = []

    # print "this is the start of helper function"
    # print boulders

    for boulder in boulders:
        boulder_dict = convert_boulder_dict(boulder)

        results.append(boulder_dict)
    # print "these are the results from helper function:"
    # print results

    return results

def convert_boulder_dict(boulder):
    """Takes a boulder object and returns
        a dictionary for converting to json"""

    results = []

    temp_dict = {}
    temp_dict["name"] = boulder.boulder_name
    temp_dict["lat"] = boulder.boulder_latitude
    temp_dict["lon"] = boulder.boulder_longitude
    temp_dict["id"] = boulder.boulder_id
    temp_dict["route"] = "/boulders/"

    boulder_id = temp_dict['id']
    routes = Route.query.filter_by(boulder_id=boulder_id).all()
    
    temp_dict["route_num"] = len(routes)
    
    num_of_routes = len(routes)
    

    results = temp_dict
    
    return results

def convert_locations_dict(locations):
    """Takes a list of location objects and returns
        a list of dictionaries for converting to json"""

    results = []

    # print "this is the start of helper function"
    # print locations

    for location in locations:
        location_dict = convert_location_dict(location)

        results.append(location_dict)

    # print "these are the results from helper function:"
    # print results

    return results

def convert_location_dict(location):
    """Takes a location object and returns
        a dictionary for converting to json"""

    results = []

    # print "this is the start of helper function"
    # print location
    
    temp_dict = {}
    temp_dict["name"] = location.location_name
    temp_dict["lat"] = location.latitude
    temp_dict["lon"] = location.longitude
    temp_dict["id"] = location.location_id
    temp_dict["route"] = "/locations/"

    results = temp_dict
        
    # print "these are the results from helper function:"
    # print results

    return results

def convert_routes_dict(routes):
    """Takes a list of route objects and returns
        a list of dictionaries for converting to json"""

    results = []

    for route in routes:
        route_dict = convert_route_dict(route)

        results.append(route_dict)

    return results

def convert_route_dict(route):
    """Takes a route object and returns a 
        dictionary for converting to json """

    results = []

    temp_dict = {}
    temp_dict["name"] = route.route_name
    temp_dict["lat"] = ""
    temp_dict["lon"] = ""
    temp_dict["id"] = route.route_id
    temp_dict["route"] = "/route/"

    results = temp_dict

    return results



