"""This module contains tests for the get_constructors() function"""

from .base_test_class import BaseTestClass


class TestGetConstructors(BaseTestClass):
    """Tests for the get_constructors() function"""
    def test_get_constructors_year(self):
        """Tests the results returned from get_constructors(year)"""
        yr_constructors = self.fp.get_constructors(2008)
        assert self.get_vals(yr_constructors) == self.get_data("constructors_2008.json")

    def test_get_constructors_bad_year(self):
        """Tests for ValueError if bad year is given to get_constructors()"""
        with self.pytest.raises(ValueError):
            self.fp.get_constructors(1949)

    def test_get_constructors(self):
        """Tests the results returned from get_constructors()"""
        all_constructors = self.fp.get_constructors()
        assert self.get_vals(all_constructors) == self.get_data("constructors.json")
