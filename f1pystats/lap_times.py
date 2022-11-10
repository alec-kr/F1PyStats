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

    def get_fastest_lap(self):
        """Returns a fastest lap"""
        print(self.results[0]["time"])
        ftime = LapTimes._get_sec(self.results[0]["time"])
        flap = self.results[0]
        for i in self.results:
            time = LapTimes._get_sec(i["time"])
            if time < ftime:
                ftime = time
                flap = i
        return (flap["position"], flap["driverId"], flap["time"])        

    def _get_sec(time_str):
        """Get seconds from time string"""
        s = 0
        num_str = ''
        for c in time_str:
            if '0' <= c and c <= '9':
                num_str += c
            elif c == ':':
                s += int(num_str)
                s *= 60
                num_str = ''
            elif c == '.':
                s += int(num_str)
                num_str = '.'
        if num_str[0] == '.':
            s += float(num_str)
        else:
            s += int(num_str)
        return s
