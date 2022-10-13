"""Contains all functions used by get_circuits()"""


class RaceCircuits:
    """Class which contains the methods which provide the details for get_circuits"""
    def __init__(self, results):
        self.results = results

    def get_circuit_name(self):
        """Returns a list of circuit names"""
        return [i["circuitName"] for i in self.results]

    def get_circuit_locality(self):
        """Returns a list of circuit locality"""
        return [i["Location"]["locality"] for i in self.results]

    def get_circuit_country(self):
        """Returns a list of circuit country"""
        return [i["Location"]["country"] for i in self.results]
