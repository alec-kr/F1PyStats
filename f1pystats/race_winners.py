'''Contains all functions used by race_winners()'''


def get_grands_prix(race_info):
    '''Returns a list of the grand prix names'''
    return [i["raceName"] for i in race_info]


def get_race_winners(race_info):
    '''Returns a list of the race winner names'''
    return [" ".join([i["Results"][0]["Driver"]["givenName"],
            i["Results"][0]["Driver"]["familyName"]]) for i in race_info]


def get_winning_constructors(race_info):
    '''Returns a list of the winning constructor'''
    return [i["Results"][0]["Constructor"]["name"] for i in race_info]


def get_race_dates(race_info):
    '''Returns a list containing the race dates'''
    return [i["date"] for i in race_info]


def get_race_laps(race_info):
    '''Returns a list containing the number of laps in each race'''
    return [i["Results"][0]["laps"] for i in race_info]


def get_race_times(race_info):
    '''Returns the length of each race'''
    return [i["Results"][0]["Time"]["time"] for i in race_info]


def get_winner_start_positions(race_info):
    '''Returns the winners starting position'''
    return [i["Results"][0]["grid"] for i in race_info]
