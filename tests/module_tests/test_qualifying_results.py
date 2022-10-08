"""This module is responsible for testing the methods in qualifying_results.py"""
import json
from f1pystats.qualifying_results import QualifyingResults
class TestQualifyingResults:
    """Contains functions for testing the methods in QualifyingResults"""
    data=""
    with open("tests/test_data/module_data/first_3_qualifying_results_2022.json",
                encoding="utf-8") as f:
        data=json.load(f)
        f.close()
    r_obj=QualifyingResults(data)
    def test_get_positions(self):
        """Test the driver positions returned from get_positions"""
        positions=self.r_obj.get_positions()
        assert positions == ['1', '2' ,'3']
    def test_get_names(self):
        """Test the driver names returned from get_names"""
        driver_names=self.r_obj.get_names()
        assert driver_names == ['Charles Leclerc', 'Max Verstappen', 'Sergio Pérez']
    def test_get_driver_numbers(self):
        """Test the driver numbers returned from get_driver_numbers"""
        driver_numbers=self.r_obj.get_driver_numbers()
        assert driver_numbers == ['16', '1', '11']
    def test_get_constructors(self):
        """Test the constructor names returned from get_constructors"""
        constructor_names=self.r_obj.get_constructors()
        assert constructor_names == ['Ferrari', 'Red Bull', 'Red Bull']
    def test_get_q1_times(self):
        """Test the  qualifying time Q1 returned from get_q1_times"""
        q1_time=self.r_obj.get_q1_times()
        assert q1_time == ['1:18.881', '1:18.580', '1:18.834']
    def test_get_q2_times(self):
        """Test the  qualifying time Q2 returned from get_q2_times"""
        q2_time=self.r_obj.get_q2_times()
        assert q2_time == ['1:18.606', '1:18.611', '1:18.340']
    def test_get_q3_times(self):
        """Test the  qualifying time Q3 returned from get_q2_times"""
        q3_time=self.r_obj.get_q3_times()
        assert q3_time == ['1:17.868', '1:18.154', '1:18.240']
