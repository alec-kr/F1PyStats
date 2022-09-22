# Return the constructor positions
def get_constructor_positions(constructor_info):
    return [i["position"] for i in constructor_info]

# Return the constructor names
def get_constructor_names(constructor_info):
    return [i["Constructor"]["name"] for i in constructor_info]

# Return the constructor points
def get_constructor_points(constructor_info):
    return [i["points"] for i in constructor_info]

# Return the constructor wins
def get_constructor_wins(constructor_info):
    return [i["wins"] for i in constructor_info]

# Return the constructor nationality
def get_constructor_nationality(constructor_info):
    return [i["Constructor"]["nationality"] for i in constructor_info]
