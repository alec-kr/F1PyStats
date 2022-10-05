"""Contains all functions used by lap_times()"""


class LapTimes:
    """Contains all methods used to get the lap timings"""

    def __init__(self, results):
        self.results = results

    def get_driver_names(self):
        """Returns a list of the driver names"""
        return [i["driverId"] for i in self.results]

    def get_driver_positions(self):
        """Returns a list of the driver position"""
        return [i["position"] for i in self.results]

    def get_lap_time(self):
        """Returns a list of the lap times"""
        return [i["time"] for i in self.results]
