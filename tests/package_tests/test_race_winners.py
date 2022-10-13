"""This module contains tests for the race_winners() function"""

from .base_test_class import BaseTestClass

class TestRaceWinners(BaseTestClass):
    """Tests for the race_winners() function"""
    def test_race_winners(self):
        """Tests the race winners returned from race_winners()"""
        winners = self.fp.race_winners(2010)
        assert self.get_vals(winners) == self.get_data("race_winners_2010.json")

    def test_race_winners_bad_year(self):
        """Tests for ValueError if bad year is given to race_winners()"""
        with self.pytest.raises(ValueError):
            self.fp.race_winners(1949)
