"""This module contains tests for the lap_times() function"""

from .base_test_class import BaseTestClass

class TestLapTimes(BaseTestClass):
    """Tests for the lap_times() function"""
    def test_lap_times(self):
        """Tests the lap times returned from lap_times()"""
        l_times = self.fp.lap_times(2010, 1, 1)
        assert self.get_vals(l_times) == self.get_data("lap_times_2010_1_1.json")

    def test_lap_times_bad_year(self):
        """Tests for ValueError if bad year is given to lap_times()"""
        with self.pytest.raises(ValueError):
            self.fp.lap_times(1949, 1, 1)
