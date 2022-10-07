"""Contains all functions used by sprint_results()"""


class SprintResults():
    """Contains all the methods used to get sprint qualifying results"""

    def __init__(self, results):
        self.results = results

    def get_driver_pos(self):
        """Returns driver position"""
        return [i["position"] for i in self.results]

    def get_driver_name(self):
        """Returns driver name"""
        return [i["Driver"]["givenName"] + " " + i["Driver"]["familyName"] for i in self.results]

    def get_driver_team(self):
        """Returns the driver team name"""
        return [i["Constructor"]["name"] for i in self.results]

    def get_driver_status(self):
        """Returns the driver sprint status"""
        return [i["status"] for i in self.results]

    def get_driver_number(self):
        """Returns the driver number"""
        return [i["Driver"]["permanentNumber"] for i in self.results]

    def get_laps(self):
        """Returns the driver sprint laps"""
        return [i["laps"] for i in self.results]

    def get_driver_grid(self):
        """Returns the driver sprint grid status"""
        return [i["grid"] for i in self.results]

    def get_driver_time(self):
        """Returns the driver sprint time"""
        time = []
        for i in self.results:
            time.append(i.get("Time", {"time": "DNF"})['time'])
        return time

    def get_driver_points(self):
        """Returns the driver sprint points"""
        return [i["points"] for i in self.results]
