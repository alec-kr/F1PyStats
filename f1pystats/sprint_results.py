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
        return [i["Driver"]["givenName"]+" "+i["Driver"]["familyName"] for i in self.results]
    def get_driver_team(self):
        """Returns the driver team name"""
        return [i["Constructor"]["name"] for i in self.results]
    def get_driver_status(self):
        """Returns the driver sprint status"""
        return [i["status"] for i in self.results]
