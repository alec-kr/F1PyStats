"""This module is responsible for testing the methods in constructor_info.py"""

import json
from f1pystats.constructor_info import ConstructorInfo


class TestConstructorInfo:
    """Contains functions for testing the methods in ConstructorInfo"""

    data = ""
    with open("tests/test_data/module_data/sample_constructor_info_2010.json",
              encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    constructor = ConstructorInfo(data)

    def test_constructors_names(self):
        """Test for the get_constructors_names methods of ConstructorInfo"""
        assert self.constructor.get_constructors_names() == ['Ferrari',
                                                             'Force India',
                                                             'HRT',
                                                             'Lotus']

    def test_constructors_nationalities(self):
        """Test for the get_constructors_nationality method of ConstructorInfo"""
        assert self.constructor.get_constructors_nationality() == ['Italian',
                                                                   'Indian',
                                                                   'Spanish',
                                                                   'Malaysian']
