"""This module contains tests for the race_table() function"""

from .base_test_class import BaseTestClass

class TestRaceTable(BaseTestClass):
    """Tests for the race_table() function"""
    def test_race_table(self):
        """Tests the race schedule returned from race_table()"""
        r_table = self.fp.race_table(2010)
        assert self.get_vals(r_table) == self.get_data("race_table_2010.json")

    def test_race_table_bad_year(self):
        """Tests for ValueError if bad year is given to race_table()"""
        with self.pytest.raises(ValueError):
            self.fp.race_table(1949)
