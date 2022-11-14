"""This module contains tests for the utility functions"""

from .base_test_class import BaseTestClass


class TestUtil(BaseTestClass):
    """Tests for the utility functions"""

    def test_get_sec(self):
        """Test seconds returned from _get_sec"""
        assert self.fp._get_sec(     "58.79") == 58.79   # Niki Lauda 1974 R9 Q
        assert self.fp._get_sec(      "1"   ) == 1       # Minimum format
        assert self.fp._get_sec("1:23:45.67") == 5025.67 # Full format
        assert self.fp._get_sec("")           == 0       # non input        
        assert self.fp._get_sec(".")          == 0       # naked decimal point

    def test_sprint_results(self):
        """Tests the results returned from sprint_results()"""
        results = self.fp.sprint_results(2021, 10)
        assert self.get_vals(results) == self.get_data("sprint_2021_10.json")

    def test_bad_sprint_value(self):
        """Tests the sprint_results() function if bad values are given"""
        with self.pytest.raises(ValueError):
            self.fp.sprint_results(2021, 9)
