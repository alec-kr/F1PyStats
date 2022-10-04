"""Contains all the functions used by get_driver()"""

class DriverInfo:
    """This is the class which stores all the functions for get_driver"""
    def __init__(self, info):
        self.info = info

    def get_drivers_names(self):
        '''Returns the driver's name list'''
        return [" ".join([i["givenName"], i["familyName"]]) for i in self.info["MRData"]["DriverTable"]["Drivers"]]

    def get_drivers_dob(self):
        '''Returns the driver's date of birth list'''
        return [i["dateOfBirth"] for i in self.info["MRData"]["DriverTable"]["Drivers"]]

    def get_drivers_nationality(self):
        """Returns the list of driver's nationality"""
        return [i["nationality"] for i in self.info["MRData"]["DriverTable"]["Drivers"]]

    def get_drivers_number(self):
        """Returns the list of driver's number"""
        return [i["permanentNumber"] for i in self.info["MRData"]["DriverTable"]["Drivers"]]
    