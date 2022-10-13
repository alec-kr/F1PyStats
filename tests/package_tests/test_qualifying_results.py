"""This module contains tests for the qualifying_results() function"""

from .base_test_class import BaseTestClass

class TestQualifyingResults(BaseTestClass):
    """Tests for the qualifying_results() function"""
    def test_qualifying_results(self):
        """Tests the results returned by qualifying_results()"""
        q_res = self.fp.qualifying_results(2021, 10)
        assert self.get_vals(q_res) == self.get_data("qualifying_2021_10.json")

    def test_get_qualifying_results_bad_year(self):
        """Tests for ValueError if bad year is given to qualifying_results()"""
        with self.pytest.raises(ValueError):
            self.fp.qualifying_results(2002, 3)
