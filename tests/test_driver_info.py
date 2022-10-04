"""Test module for testing methods DriverInfo class from driver_info folder """
import json
from f1pystats.driver_info import DriverInfo


class TestDriverInfo:
    """Class containaing the functions for testing the DriverInfo class methods"""
    
    data = ""
    with open("tests/test_data/dummy_drivers_ifno.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()
        
    driver = DriverInfo(data)
    
    def test_driver_names(self):
        """Test for the get_driver_names methods of DriverInfo"""
        assert self.driver.get_driver_names() == ['Jean Alesi', 'Rubens Barrichello', 'Luciano Burti']
    
    def test_driver_dob(self):
        """Test for the get_driver_dob method of DriverInfo"""
        assert self.driver.get_drivers_dob() == ['1964-06-11', '1972-05-23', '1975-03-05']
    
    def test_driver_nationality(self):
        """Test for the get_driver_nationality method of DriverInfo"""
        assert self.driver.get_driver_nationality() == ['French', 'Brazilian', 'Brazilian']
    
    def test_driver_number(self):
        """Test for the get_driver_number method of DriverInfo
        WARNING: this method can return key error if used without proper caution cause some data can't 
        have the permanent error.
        """
        assert self.driver.get_drivers_number() == ['23', '34', '45']
    
    