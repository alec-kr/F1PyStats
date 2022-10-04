"""Contains all functions used by driver_standings()"""


class DriverResults:
    """Contains all methods used to get driver results"""

    def __init__(self, results):
        self.results = results

    def get_driver_positions(self):
        """Returns the driver positions"""
        return [i["position"] for i in self.results]

    def get_driver_names(self):
        """Returns the driver names"""
        return [
            " ".join([i["Driver"]["givenName"], i["Driver"]["familyName"]]) for i in self.results
        ]

    def get_driver_points(self):
        """Returns the points obtained by each driver"""
        return [i["points"] for i in self.results]

    def get_driver_teams(self):
        """Returns the driver's team name"""
        return [i["Constructors"][0]["name"] for i in self.results]

    def get_driver_nationality(self):
        """Returns the driver's nationality"""
        return [i["Driver"]["nationality"] for i in self.results]

    def get_driver_wins(self):
        """Returns the total wins for each driver"""
        return [i["wins"] for i in self.results]
