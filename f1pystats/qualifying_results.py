"""Contains all functions used by qualifying_results()"""


class QualifyingResults:
    """Class which contains the methods which provide the details qualifying_results()"""
    def __init__(self, results):
        self.results = results

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

    def get_q1_times(self):
        """Returns a list of Q1 timings"""
        r_q1 = []
        for i in self.results:
            if "Q1" in i:
                r_q1.append(i["Q1"])
        return r_q1

    def get_q2_times(self):
        """Returns a list of Q2 timings"""
        r_q2 = []
        for i in self.results:
            if "Q2" in i:
                r_q2.append(i["Q2"])
            else:
                r_q2.append('')
        return r_q2

    def get_q3_times(self):
        """Returns a list of Q3 timings"""
        r_q3 = []
        for i in self.results:
            if "Q3" in i:
                r_q3.append(i["Q3"])
            else:
                r_q3.append('')
        return r_q3
