# Return the constructor positions
def get_constructor_positions(constructor_info):
    positions_list = []

    for i in range(len(constructor_info)):
        positions_list.append(constructor_info[i]["position"])
    
    return positions_list

# Return the constructor names
def get_constructor_names(constructor_info):
    names_list = []

    for i in range(len(constructor_info)):
        names_list.append(constructor_info[i]["Constructor"]["name"])
    
    return names_list

# Return the constructor points
def get_constructor_points(constructor_info):
    points_list = []

    for i in range(len(constructor_info)):
        points_list.append(constructor_info[i]["points"])
    
    return points_list

# Return the constructor wins
def get_constructor_wins(constructor_info):
    wins_list = []

    for i in range(len(constructor_info)):
        wins_list.append(constructor_info[i]["wins"])
    
    return wins_list

# Return the constructor nationality
def get_constructor_nationality(constructor_info):
    nationality_list = []

    for i in range(len(constructor_info)):
        nationality_list.append(constructor_info[i]["Constructor"]["nationality"])
    
    return nationality_list