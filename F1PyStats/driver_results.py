# Return the driver positions
def get_driver_positions(driver_info):
    positions_list = []

    for i in range(len(driver_info)):
        positions_list.append(driver_info[i]["position"])
    
    return positions_list

# Return the driver names
def get_driver_names(driver_info):
    names_list = []

    for i in range(len(driver_info)):
        f_name = driver_info[i]["Driver"]["givenName"]
        l_name = driver_info[i]["Driver"]["familyName"]

        names_list.append(" ".join([f_name, l_name]))
    
    return names_list

# Return the points obtained by each driver
def get_driver_points(driver_info):
    points_list = []

    for i in range(len(driver_info)):
        points_list.append(driver_info[i]["points"])
    
    return points_list

def get_driver_teams(driver_info):
    teams_list = []

    for i in range(len(driver_info)):
        teams_list.append(driver_info[i]["Constructors"][0]["name"])
    
    return teams_list

def get_driver_nationality(driver_info):
    nationality_list = []

    for i in range(len(driver_info)):
        nationality_list.append(driver_info[i]["Driver"]["nationality"])
    
    return nationality_list

def get_driver_wins(driver_info):
    wins_list = []

    for i in range(len(driver_info)):
        wins_list.append(driver_info[i]["wins"])
    
    return wins_list 