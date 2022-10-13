"""This module contains tests for the get_drivers() function"""

from .base_test_class import BaseTestClass

class TestGetDrivers(BaseTestClass):
    """Tests for the get_drivers() function"""
    def test_get_drivers_race(self):
        """Tests the drivers in a race returned by get_drivers(year, race_round)"""
        drivers = self.fp.get_drivers(2016, 11)
        assert self.get_vals(drivers) == self.get_data("drivers_2016_11.json")

    def test_get_drivers_year(self):
        """Tests the drivers in a specific year returned from get_drivers(year)"""
        drivers = self.fp.get_drivers(2010)
        assert self.get_vals(drivers) == self.get_data("drivers_2010.json")

    def test_get_drivers_bad_year(self):
        """Tests for ValueError if bad year is given to get_drivers()"""
        with self.pytest.raises(ValueError):
            self.fp.get_drivers(1949)
