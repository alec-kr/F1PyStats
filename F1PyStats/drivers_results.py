from bs4 import Tag

# Return the driver positions
def get_positions(table):
    positions_list = []
    for item in table:
        if isinstance(item, Tag):
            position = item.find("td", {"class": "dark"})

            if position is not None:
                positions_list.append(position.decode_contents())
    
    return positions_list

# Return the driver names
def get_names(table):
    names_list = []
    for item in table:
        if isinstance(item, Tag):
            f_name = item.find("span", {"class": "hide-for-tablet"})
            l_name = item.find("span", {"class": "hide-for-mobile"})

            if f_name is not None and l_name is not None:
                names_list.append(f_name.decode_contents() + " " + l_name.decode_contents())

    return names_list

# Return the drivers' corresponding teams
def get_driver_teams(table):
    teams_list = []
    for item in table:
        if isinstance(item, Tag):
            team_name = item.find("a", {"class": "grey semi-bold uppercase ArchiveLink"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list

# Returns a list of the drivers' nationalities
def get_nationalities(table):
    nationality_list = []
    for item in table:
        if isinstance(item, Tag):
            nationality = item.find("td", {"class": "dark semi-bold uppercase"})

            if nationality is not None:
                nationality_list.append(nationality.decode_contents())
    
    return nationality_list

# Return the points obtained by each driver
def get_points(table):
    points_list = []
    for item in table:
        if isinstance(item, Tag):
            curr_points = item.find("td", {"class": "dark bold"})

            if curr_points is not None:
                points_list.append(curr_points.decode_contents())

    return points_list