# Return the driver positions
def get_driver_positions(driver_info):
    return [i["position"] for i in driver_info]

# Return the driver names
def get_driver_names(driver_info):
    return [" ".join([i["Driver"]["givenName"], i["Driver"]["familyName"]]) for i in driver_info]

# Return the points obtained by each driver
def get_driver_points(driver_info):
    return [i["points"] for i in driver_info]

def get_driver_teams(driver_info):
    return [i["Constructors"][0]["name"] for i in driver_info]

def get_driver_nationality(driver_info):
    return [i["Driver"]["nationality"] for i in driver_info]

def get_driver_wins(driver_info):
    return [i["wins"] for i in driver_info]
