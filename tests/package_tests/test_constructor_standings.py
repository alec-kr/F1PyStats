"""This module contains tests for the constructor_standings() function"""

from .base_test_class import BaseTestClass


class TestConstructorStandings(BaseTestClass):
    """Tests for the constructor_standings() function"""
    def test_constructor_standings(self):
        """Tests the constructor standings returned from constructor_standings()"""
        winner = self.fp.constructor_standings(2008)
        assert self.get_vals(winner) == self.get_data("constructor_standings_2008.json")

    def test_constructor_standings_bad_year(self):
        """Tests for ValueError if bad year is given to constructor_standings()"""
        with self.pytest.raises(ValueError):
            self.fp.constructor_standings(1949)
