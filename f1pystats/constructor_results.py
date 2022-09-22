'''Contains all functions used by constructor_standings()'''


def get_constructor_positions(constructor_info):
    '''Returns the constructor positions'''
    return [i["position"] for i in constructor_info]


def get_constructor_names(constructor_info):
    '''Returns the constructor names'''
    return [i["Constructor"]["name"] for i in constructor_info]


def get_constructor_points(constructor_info):
    '''Returns the constructor points'''
    return [i["points"] for i in constructor_info]


def get_constructor_wins(constructor_info):
    '''Returns the constructor wins'''
    return [i["wins"] for i in constructor_info]


def get_constructor_nationality(constructor_info):
    '''Returns the constructor nationality'''
    return [i["Constructor"]["nationality"] for i in constructor_info]
