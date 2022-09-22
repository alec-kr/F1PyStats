'''Contains all functions used by driver_standings()'''


def get_driver_positions(driver_info):
    '''Returns the driver positions'''
    return [i["position"] for i in driver_info]


def get_driver_names(driver_info):
    '''Returns the driver names'''
    return [" ".join([i["Driver"]["givenName"],
            ["Driver"]["familyName"]]) for i in driver_info]


def get_driver_points(driver_info):
    '''Returns the points obtained by each driver'''
    return [i["points"] for i in driver_info]


def get_driver_teams(driver_info):
    '''Returns the driver's team name'''
    return [i["Constructors"][0]["name"] for i in driver_info]


def get_driver_nationality(driver_info):
    '''Returns the driver's nationality'''
    return [i["Driver"]["nationality"] for i in driver_info]


def get_driver_wins(driver_info):
    '''Returns the total wins for each driver'''
    return [i["wins"] for i in driver_info]
