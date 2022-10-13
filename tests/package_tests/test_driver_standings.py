"""This module contains tests for the driver_standings() function"""

from .BaseTestClass import BaseTestClass

class TestDriverStandings(BaseTestClass):
    def test_driver_standings(self):
        """Tests the driver standings returned from driver_standings()"""
        standings = self.fp.driver_standings(2010)
        assert self.get_vals(standings) == self.get_data("driver_standings_2010.json")

    def test_driver_standings_bad_year(self):
        """Tests for ValueError if bad year is given to driver_standings()"""
        with self.pytest.raises(ValueError):
            self.fp.driver_standings(1949)
