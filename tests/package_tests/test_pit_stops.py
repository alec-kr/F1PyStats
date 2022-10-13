"""This module contains tests for the pit_stops() function"""

from .base_test_class import BaseTestClass


class TestPitStops(BaseTestClass):
    """Tests for the pit_stops() function"""
    def test_pit_stops_race(self):
        """Tests the pit stops in a race returned from pit_stops(year, race)"""
        p_stops = self.fp.pit_stops(2012, 1)
        assert self.get_vals(p_stops) == self.get_data("pit_stops_2012_1.json")

    def test_pit_stops_bad_year(self):
        """Tests for ValueError if bad year is given to pit_stops()"""
        with self.pytest.raises(ValueError):
            self.fp.pit_stops(2011, 2)

    def test_pit_stops_number(self):
        """Tests an interval of pit stops in a race,
        returned from pit_stops(year, race, stop_number)"""
        p_stops = self.fp.pit_stops(2012, 1, 3)
        assert self.get_vals(p_stops) == self.get_data("pit_stops_2012_1_3.json")
