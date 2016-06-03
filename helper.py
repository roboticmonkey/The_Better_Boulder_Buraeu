"""Helper functions for Server.py"""

def convert_sublocations_dict(sub_locations):
    """Takes a list of sub location objects and returns
        a list of dictionaries for converting to json"""

    results = []

    print "this is the start of helper function"
    print sub_locations

    for sub in sub_locations:
        temp_dict = {}
        temp_dict["name"] = sub.sub_location_name
        temp_dict["lat"] = sub.sub_latitude
        temp_dict["lon"] = sub.sub_longitude
        temp_dict["id"] = sub.sub_location_id
        temp_dict["route"] = "/sub_locations/"

        results.append(temp_dict)
    print "these are the results from helper function:"
    print results

    return results

def convert_boulders_dict(boulders):
    """Takes a list of boulder objects and returns
        a list of dictionaries for converting to json"""

    results = []

    print "this is the start of helper function"
    print boulders

    for boulder in boulders:
        temp_dict = {}
        temp_dict["name"] = boulder.boulder_name
        temp_dict["lat"] = boulder.boulder_latitude
        temp_dict["lon"] = boulder.boulder_longitude
        temp_dict["id"] = boulder.boulder_id
        temp_dict["route"] = "/boulders/"

        results.append(temp_dict)
    print "these are the results from helper function:"
    print results

    return results

def convert_locations_dict(locations):
    """Takes a list of location objects and returns
        a list of dictionaries for converting to json"""

    results = []

    print "this is the start of helper function"
    print locations

    for location in locations:
        # temp_dict = {}
        # temp_dict["name"] = location.location_name
        # temp_dict["lat"] = location.latitude
        # temp_dict["lon"] = location.longitude
        # temp_dict["id"] = location.location_id
        # temp_dict["route"] = "/locations/"
        convert_location_dict(location)

        results.append(temp_dict)

    print "these are the results from helper function:"
    print results

    return results

def convert_location_dict(location):
    """Takes a list of location object and returns
        a dictionary for converting to json"""

    results = []

    print "this is the start of helper function"
    print location

    
    temp_dict = {}
    temp_dict["name"] = location.location_name
    temp_dict["lat"] = location.latitude
    temp_dict["lon"] = location.longitude
    temp_dict["id"] = location.location_id
    temp_dict["route"] = "/locations/"

    results.append(temp_dict)
        
    print "these are the results from helper function:"
    print results

    return results
