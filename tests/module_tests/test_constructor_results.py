"""This module is responsible for testing the methods in constructor_results.py"""

import json

from f1pystats.constructor_results import ConstructorResults


class TestConstructorResults:
    """Contains functions for testing the methods in ConstructorResults"""

    data = ""
    with open("tests/test_data/module_data/top_3_constructors_2008.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    c_res = ConstructorResults(data)

    def test_constructor_positions(self):
        """Test the positions returned by get_constructor_positions"""
        positions = self.c_res.get_constructor_positions()
        assert positions == ["1", "2", "3"]

    def test_constructor_names(self):
        """Test the names returned by get_constructor_names"""
        c_names = self.c_res.get_constructor_names()
        assert c_names == ["Ferrari", "McLaren", "BMW Sauber"]

    def test_constructor_points(self):
        """Test the points returned by get_constructor_points"""
        points = self.c_res.get_constructor_points()
        assert points == ["172", "151", "135"]

    def test_constructor_wins(self):
        """Test the wins returned by get_constructor_wins"""
        wins = self.c_res.get_constructor_wins()
        assert wins == ["8", "6", "1"]

    def test_constructor_nationalities(self):
        """Test the nationalities returned by get_constructor_nationalities"""
        positions = self.c_res.get_constructor_nationality()
        assert positions == ["Italian", "British", "German"]
