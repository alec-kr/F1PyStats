'''Contains all functions used by pit_stops()'''


class PitStops():
    '''Contains all methods used to get the pit stop info'''
    def __init__(self, results):
        self.results = results

    def get_driver_names(self):
        '''Returns a list of the driver names'''
        return [i["driverId"] for i in self.results]

    def get_stop_numbers(self):
        '''Return the pitstop numbers'''
        return [i["stop"] for i in self.results]

    def get_lap_numbers(self):
        '''Returns a list of lap numbers'''
        return [i["lap"] for i in self.results]

    def get_times(self):
        '''Returns a list of times'''
        return [i["time"] for i in self.results]

    def get_durations(self):
        '''Returns the duration of each pitstop'''
        return [i["duration"] for i in self.results]
