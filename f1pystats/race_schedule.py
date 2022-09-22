# Return the round number for each race
def get_race_round(table):
    return [i["round"] for i in table]

# Return the race names
def get_race_names(table):
    return [i["raceName"] for i in table]

# Return the race dates
def get_race_schedule_dates(table):
    return [i["date"] for i in table]

# Return the race circuit names
def get_race_circuits(table):
    return [i["Circuit"]["circuitName"] for i in table]

# Return the race times
def get_race_schedule_times(table):
    return [i["time"] for i in table]

# Return the host country of the race
def get_race_countries(table):
    return [i["Circuit"]["Location"]["country"] for i in table]

# Return the local area name where each race is hosted
def get_race_locality(table):
    return [i["Circuit"]["Location"]["locality"] for i in table]
