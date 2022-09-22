'''Contains all functions used by race_table()'''


def get_race_round(table):
    '''Returns the round number for each race'''
    return [i["round"] for i in table]


def get_race_names(table):
    '''Returns the race names'''
    return [i["raceName"] for i in table]


def get_race_schedule_dates(table):
    '''Returns the race dates'''
    return [i["date"] for i in table]


def get_race_circuits(table):
    '''Returns the race circuit names'''
    return [i["Circuit"]["circuitName"] for i in table]


def get_race_schedule_times(table):
    '''Returns race times'''
    return [i["time"] for i in table]


def get_race_countries(table):
    '''Returns the host country of each race'''
    return [i["Circuit"]["Location"]["country"] for i in table]


def get_race_locality(table):
    '''Returns the local area hosting each race'''
    return [i["Circuit"]["Location"]["locality"] for i in table]
