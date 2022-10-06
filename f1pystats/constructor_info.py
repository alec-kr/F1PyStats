"""Contains all the functions used by get_constructors()"""


class ConstructorInfo:
    """This is the class which stores all the functions for get_constructors"""
    def __init__(self, info):
        self.info = info

    def get_constructors_names(self):
        """Returns the list of constructor names"""
        return [i["name"] for i in self.info]

    def get_constructors_nationality(self):
        """Returns the list constructor nationalities"""
        return [i["nationality"] for i in self.info]
