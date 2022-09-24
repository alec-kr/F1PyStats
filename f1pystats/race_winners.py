'''Contains all functions used by race_winners()'''


class RaceWinners():
    '''Contains all methods used to get the race winners'''
    def __init__(self, results):
        self.results = results

    def get_grands_prix(self):
        '''Returns a list of the grand prix names'''
        return [i["raceName"] for i in self.results]

    def get_race_winners(self):
        '''Returns a list of the race winner names'''
        return [" ".join([i["Results"][0]["Driver"]["givenName"],
                i["Results"][0]["Driver"]["familyName"]])
                for i in self.results]

    def get_winning_constructors(self):
        '''Returns a list of the winning constructor'''
        return [i["Results"][0]["Constructor"]["name"]
                for i in self.results]

    def get_race_dates(self):
        '''Returns a list containing the race dates'''
        return [i["date"] for i in self.results]

    def get_race_laps(self):
        '''Returns a list containing the number of laps in each race'''
        return [i["Results"][0]["laps"] for i in self.results]

    def get_race_times(self):
        '''Returns the length of each race'''
        return [i["Results"][0]["Time"]["time"] for i in self.results]

    def get_winner_start_positions(self):
        '''Returns the winners starting position'''
        return [i["Results"][0]["grid"] for i in self.results]
