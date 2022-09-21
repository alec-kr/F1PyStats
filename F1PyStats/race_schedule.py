# Return the round number for each race
def get_race_round(table):
    rounds = []

    for i in range(len(table)):
        race_round = table[i]["round"]
        rounds.append(race_round)
    
    return rounds

# Return the race names
def get_race_names(table):
    race_names = []

    for i in range(len(table)):
        race_name = table[i]["raceName"]
        race_names.append(race_name)
    
    return race_names

# Return the race dates
def get_race_schedule_dates(table):
    race_dates = []

    for i in range(len(table)):
        race_date = table[i]["date"]
        race_dates.append(race_date)
    
    return race_dates

# Return the race circuit names
def get_race_circuits(table):
    circuits = []

    for i in range(len(table)):
        race_circuit = table[i]["Circuit"]["circuitName"]
        circuits.append(race_circuit)
    
    return circuits

# Return the race times
def get_race_schedule_times(table):
    times = []

    for i in range(len(table)):
        race_time = table[i]["time"]
        times.append(race_time)
    
    return times

# Return the host country of the race
def get_race_countries(table):
    countries = []

    for i in range(len(table)):
        country = table[i]["Circuit"]["Location"]["country"]
        countries.append(country)
    
    return countries

# Return the local area name where each race is hosted
def get_race_locality(table):
    localities = []

    for i in range(len(table)):
        locality = table[i]["Circuit"]["Location"]["locality"]
        localities.append(locality)
    
    return localities
