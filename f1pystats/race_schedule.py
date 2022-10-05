"""Contains all functions used by race_table()"""


class RaceSchedule:
    """Contains all methods used to get the race schedule"""

    def __init__(self, schedule):
        self.schedule = schedule

    def get_race_round(self):
        """Returns the round number for each race"""
        return [i["round"] for i in self.schedule]

    def get_race_names(self):
        """Returns the race names"""
        return [i["raceName"] for i in self.schedule]

    def get_race_schedule_dates(self):
        """Returns the race dates"""
        return [i["date"] for i in self.schedule]

    def get_race_circuits(self):
        """Returns the race circuit names"""
        return [i["Circuit"]["circuitName"] for i in self.schedule]

    def get_race_schedule_times(self):
        """Returns race times"""
        return [i["time"] for i in self.schedule]

    def get_race_countries(self):
        """Returns the host country of each race"""
        return [i["Circuit"]["Location"]["country"] for i in self.schedule]

    def get_race_locality(self):
        """Returns the local area hosting each race"""
        return [i["Circuit"]["Location"]["locality"] for i in self.schedule]
