"""Contains all functions used by qualifying_results()"""
class QualifyingResults:
    """Class which contains the methods which provide the details qualifying_results()"""
    def __init__(self,results):
        self.results=results
    def get_positions(self):
        """Returns a list of driver positions"""
        return [i["position"] for i in self.results]
    def get_names(self):
        """Returns a list of driver names"""
        return [" ".join([i["Driver"]["givenName"],
            i["Driver"]["familyName"]]) for i in self.results]
    def get_driver_numbers(self):
        """Returns a list of driver numbers"""
        return [i["number"] for i in self.results]
    def get_constructors(self):
        """Returns the list of name of the constructors"""
        return [i["Constructor"]["name"] for i in self.results]
    def get_qualifying_times(self):
        """Returns a list of tuple of Q1,Q2,Q3 timings"""
        return [(i["Q1"],i["Q2"],i["Q3"]) for i in self.results]
