"""Test module for testing methods DriverInfo class from driver_info folder """
import json
from f1pystats.driver_info import DriverInfo


class TestDriverInfo:
    """Class containaing the functions for testing the DriverInfo class methods"""

    data = ""
    with open("tests/test_data/sample_drivers_info_2000.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    driver = DriverInfo(data)

    def test_drivers_names(self):
        """Test for the get_drivers_names methods of DriverInfo"""
        assert self.driver.get_drivers_names() == ['Jean Alesi',
                                                   'Rubens Barrichello',
                                                   'Luciano Burti',
                                                   'David Coulthard']

    def test_drivers_dob(self):
        """Test for the get_drivers_dob method of DriverInfo"""
        assert self.driver.get_drivers_dob() == ['1964-06-11',
                                                 '1972-05-23',
                                                 '1975-03-05',
                                                 '1971-03-27']

    def test_drivers_nationality(self):
        """Test for the get_drivers_nationality method of DriverInfo"""
        assert self.driver.get_drivers_nationality() == ['French',
                                                         'Brazilian',
                                                         'Brazilian',
                                                         'British']

    def test_drivers_number(self):
        """Test for the get_drivers_number method of DriverInfo"""
        assert self.driver.get_drivers_number() == ['23', '34', '45', None]
