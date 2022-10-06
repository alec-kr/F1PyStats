"""This module is responsible for testing functions in the f1pystats package"""

import f1pystats.f1pystats as fp
import json

class TestPackage:
    """These class methods are used to test the functions in f1pystats"""

    def __get_vals(self, json_data):
        """Convert the API's JSON values into a nested list"""
        return json_data.values.tolist()
    
    def __get_data(self, file_name):
        """Read and store the data in the test data files"""
        data = ""
        with open("tests/test_data/api_data/{}".format(file_name), encoding="utf-8") as f:
            data = json.load(f)
            f.close()
        
        return data

    def test_constructor_standings(self):
        """Tests the constructor standings returned from constructor_standings()"""
        winner = fp.constructor_standings(2008).head(3)
        assert self.__get_vals(winner) == self.__get_data("constructor_standings_2008.json")

    def test_driver_standings(self):
        """Tests the driver standings returned from driver_standings()"""
        standings = fp.driver_standings(2010).head(3)
        assert self.__get_vals(standings) == self.__get_data("driver_standings_2010.json")

    def test_race_winners(self):
        """Tests the race winners returned from race_winners()"""
        winners = fp.race_winners(2010).head(3)
        assert self.__get_vals(winners) == self.__get_data("three_race_winners_2010.json")

    def test_race_table(self):
        """Tests the race schedule returned from race_table()"""
        r_table = fp.race_table(2010).head(3)
        assert self.__get_vals(r_table) == self.__get_data("race_table_2010.json")

    def test_lap_times(self):
        """Tests the lap times returned from lap_times()"""
        l_times = fp.lap_times(2010, 1, 1).head(3)
        assert self.__get_vals(l_times) == self.__get_data("lap_times_2010_1_1.json")

    def test_pit_stops_race(self):
        """Tests the pit stops in a race returned from pit_stops(year, race)"""
        p_stops = fp.pit_stops(2012, 1).head(3)
        assert self.__get_vals(p_stops) == self.__get_data("pit_stops_2012_1.json")

    def test_pit_stops_number(self):
        """Tests an interval of pit stops in a race, returned from pit_stops(year, race, stop_number)"""
        p_stops = fp.pit_stops(2012, 1, 3).head(3)
        assert self.__get_vals(p_stops) == self.__get_data("pit_stops_2012_1_3.json")

    def test_finishing_status_year(self):
        """Tests a year's finishing status returned from finishing_status(year)"""
        f_status = fp.finishing_status(2008).head(3)
        assert self.__get_vals(f_status) == self.__get_data("finishing_status_2008.json")

    def test_finishing_status_race(self):
        """Tests a race's finishing status returned from finishing_status(year, race_round)"""
        f_status = fp.finishing_status(2008, 1).head(3)
        assert self.__get_vals(f_status) == self.__get_data("finishing_status_2008_1.json")

    def test_get_drivers_race(self):
        """Tests the drivers in a race returned by get_drivers(year, race_round)"""
        drivers = fp.get_drivers(2016, 11).head(3)
        assert self.__get_vals(drivers) == self.__get_data("drivers_2016_11.json")

    def test_get_drivers_year(self):
        """Tests the drivers in a specific year returned from get_drivers(year)"""
        drivers = fp.get_drivers(2010).head(3)
        assert self.__get_vals(drivers) == [
            ["Jaime Alguersuari", None, "Spanish", "1990-03-23"],
            ["Fernando Alonso", "14", "Spanish", "1981-07-29"],
            ["Rubens Barrichello", None, "Brazilian", "1972-05-23"]
        ]
