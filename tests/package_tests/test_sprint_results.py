"""This module contains tests for the sprint_results() function"""

from .base_test_class import BaseTestClass

class TestSprintResults(BaseTestClass):
    """Tests for the sprint_results() function"""
    def test_sprint_results(self):
        """Tests the results returned from sprint_results()"""
        results = self.fp.sprint_results(2021, 10)
        assert self.get_vals(results) == self.get_data("sprint_2021_10.json")

    def test_bad_sprint_value(self):
        """Tests the sprint_results() function if bad values are given"""
        with self.pytest.raises(ValueError):
            self.fp.sprint_results(2021, 9)
