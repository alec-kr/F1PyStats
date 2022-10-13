"""This module contains tests for the get_circuits() function"""

from .base_test_class import BaseTestClass

class TestGetCircuits(BaseTestClass):
    """Tests for the get_circuits() function"""
    def test_get_all_circuits(self):
        """Tests the circuits returned by get_circuits()"""
        circuits = self.fp.get_circuits()
        assert self.get_vals(circuits) == self.get_data("all_circuits.json")

    def test_get_circuits(self):
        """Tests the circuits returned by get_circuits(year)"""
        circuits = self.fp.get_circuits(2021)
        assert self.get_vals(circuits) == self.get_data("circuits_2021.json")

    def test_get_circuits_bad_year(self):
        """Tests for ValueError if bad year is given to get_circuits()"""
        with self.pytest.raises(ValueError):
            self.fp.get_circuits(1949)
