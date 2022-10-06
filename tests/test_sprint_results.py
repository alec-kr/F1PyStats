"""This module is responsible for testing the methods in sprint_results.py"""

import json
from f1pystats.sprint_results import SprintResults


class TestSprintResults:
    """Contains functions for testing the methods in SprintResults"""

    data = ""
    with open("tests/test_data/top_3_sprint_2022_11.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    s_result = SprintResults(data)

    def test_get_driver_pos(self):
        """Test the driver position returned by get_driver_pos"""
        driver_pos = self.s_result.get_driver_pos()
        assert driver_pos == [
            "1", "2", "3"
        ]

    def test_get_driver_name(self):
        """Test the driver name returned by get_driver_name"""
        name = self.s_result.get_driver_name()
        assert name == [
            "Max Verstappen",
            "Charles Leclerc",
            "Carlos Sainz"
        ]

    def test_get_driver_team(self):
        """Test the driver team returned by get_driver_team"""
        team = self.s_result.get_driver_team()
        assert team == [
            "Red Bull",
            "Ferrari",
            "Ferrari"
        ]
    
    def test_get_driver_status(self):
        """Test the driver status returned by get_driver_status"""
        status = self.s_result.get_driver_status()
        assert status == [
            "Finished",
            "Finished",
            "Finished"
        ]
