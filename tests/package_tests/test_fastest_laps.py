"""This module contains tests for the fastest_laps() function"""

from .base_test_class import BaseTestClass


class TestFastestLaps(BaseTestClass):
    """Tests for the fastest_laps() function"""
    def test_fastest_laps(self):
        """Tests the fastest lap returned from fastest_laps()"""
        fastest = self.fp.fastest_laps(2010,1)
        assert self.get_vals(fastest) == self.get_data("fastest_lap_2010_round_1.json")

    def test_fastest_laps_bad_year(self):
        """Tests for ValueError if bad year is given to fastest_laps()"""
        with self.pytest.raises(ValueError):
            self.fp.fastest_laps(1949,1)
