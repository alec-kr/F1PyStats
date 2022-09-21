# Return the grand prix names
def get_grands_prix(race_info):
    gp_list = []

    for i in range(len(race_info)):
        gp_list.append(race_info[i]["raceName"])
    
    return gp_list

# Return the race winner names
def get_race_winners(race_info):
    winners_list = []

    for i in range(len(race_info)):
        f_name = race_info[i]["Results"][0]["Driver"]["givenName"]
        l_name = race_info[i]["Results"][0]["Driver"]["familyName"]
        winners_list.append(" ".join([f_name, l_name]))
    
    return winners_list

# Return the winning constructor
def get_winning_constructors(race_info):
    constructors_list = []

    for i in range(len(race_info)):
        constructor_name = race_info[i]["Results"][0]["Constructor"]["name"]
        constructors_list.append(constructor_name)
    
    return constructors_list

# Return the race dates
def get_race_dates(race_info):
    dates_list = []

    for i in range(len(race_info)):
        dates_list.append(race_info[i]["date"])
    
    return dates_list

# Return the number of laps in each race
def get_race_laps(race_info):
    laps_list = []

    for i in range(len(race_info)):
        laps_list.append(race_info[i]["Results"][0]["laps"])
    
    return laps_list

# Return the length of each race
def get_race_times(race_info):
    times_list = []

    for i in range(len(race_info)):
        times_list.append(race_info[i]["Results"][0]["Time"]["time"])
    
    return times_list

# Return the winners starting position
def get_winner_start_positions(race_info):
    positions_list = []

    for i in range(len(race_info)):
        constructor_name = race_info[i]["Results"][0]["grid"]
        positions_list.append(constructor_name)
    
    return positions_list