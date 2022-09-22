# Return the grand prix names
def get_grands_prix(race_info):
    return [i["raceName"] for i in race_info]

# Return the race winner names
def get_race_winners(race_info):
    winners_list = []

    for i in race_info:
        f_name = i["Results"][0]["Driver"]["givenName"]
        l_name = i["Results"][0]["Driver"]["familyName"]
        winners_list.append(" ".join([f_name, l_name]))
    
    return winners_list

# Return the winning constructor
def get_winning_constructors(race_info):
    return [i["Results"][0]["Constructor"]["name"] for i in race_info]

# Return the race dates
def get_race_dates(race_info):
    return [i["date"] for i in race_info]

# Return the number of laps in each race
def get_race_laps(race_info):
    return [i["Results"][0]["laps"] for i in race_info]

# Return the length of each race
def get_race_times(race_info):
    return [i["Results"][0]["Time"]["time"] for i in race_info]

# Return the winners starting position
def get_winner_start_positions(race_info):
    return [i["Results"][0]["grid"] for i in race_info]
