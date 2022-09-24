'''Contains all functions used by constructor_standings()'''


class ConstructorResults:
    '''Contains all methods used to get constructor results'''
    def __init__(self, results):
        self.results = results

    def get_constructor_positions(self):
        '''Returns the constructor positions'''
        return [i["position"] for i in self.results]

    def get_constructor_names(self):
        '''Returns the constructor names'''
        return [i["Constructor"]["name"] for i in self.results]

    def get_constructor_points(self):
        '''Returns the constructor points'''
        return [i["points"] for i in self.results]

    def get_constructor_wins(self):
        '''Returns the constructor wins'''
        return [i["wins"] for i in self.results]

    def get_constructor_nationality(self):
        '''Returns the constructor nationality'''
        return [i["Constructor"]["nationality"] for i in self.results]
