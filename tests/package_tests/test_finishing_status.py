"""This module contains tests for the finishing_status() function"""

from .base_test_class import BaseTestClass


class TestFinishingStatus(BaseTestClass):
    """Tests for the finishing_status() function"""
    def test_finishing_status_year(self):
        """Tests a year's finishing status returned from finishing_status(year)"""
        f_status = self.fp.finishing_status(2008)
        assert self.get_vals(f_status) == self.get_data("finishing_status_2008.json")

    def test_finishing_status_bad_year(self):
        """Tests for ValueError if bad year is given to finishing_status()"""
        with self.pytest.raises(ValueError):
            self.fp.finishing_status(1949)

    def test_finishing_status_race(self):
        """Tests a race's finishing status returned from finishing_status(year, race_round)"""
        f_status = self.fp.finishing_status(2008, 1)
        assert self.get_vals(f_status) == self.get_data("finishing_status_2008_1.json")
