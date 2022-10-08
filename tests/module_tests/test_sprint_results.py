"""This module is responsible for testing the methods in sprint_results.py"""

import json
from f1pystats.sprint_results import SprintResults


class TestSprintResults:
    """Contains functions for testing the methods in SprintResults"""

    data = ""
    with open("tests/test_data/module_data/top_3_sprint_2022_11.json", encoding='utf-8') as f:
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

    def test_get_driver_number(self):
        """Test the driver number returned by get_driver_number"""
        number = self.s_result.get_driver_number()
        assert number == [
            "33",
            "16",
            "55"
        ]

    def test_get_laps(self):
        """Test the driver laps returned by get_laps"""
        laps = self.s_result.get_laps()
        assert laps == [
            "23",
            "23",
            "23"
        ]

    def test_get_driver_grid(self):
        """Test the driver grid position returned by get_driver_grid"""
        grid = self.s_result.get_driver_grid()
        assert grid == [
            "1",
            "2",
            "3"
        ]

    def test_get_driver_time(self):
        """Test the driver time returned by get_driver_time"""
        driver_time = self.s_result.get_driver_time()
        assert driver_time == [
            "26:30.059",
            "+1.675",
            "+5.644"
        ]

    def test_get_driver_points(self):
        """Test the driver points returned by get_driver_points"""
        points = self.s_result.get_driver_points()
        assert points == [
            "8",
            "7",
            "6"
        ]
