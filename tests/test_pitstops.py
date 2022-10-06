"""This module is responsible for testing the methods in pit_stops.py"""

import json
from f1pystats.pit_stops import PitStops


class TestPitStops:
    """Contains functions for testing the methods in PitStops"""

    data = ""
    with open("tests/test_data/module_data/first_3_stops_2019_melbourne.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    p_stops = PitStops(data)

    def test_driver_names(self):
        """Test the names returned by get_driver_names"""
        names = self.p_stops.get_driver_names()
        assert names == ["kubica", "ricciardo", "raikkonen"]

    def test_stop_numbers(self):
        """Test the stop numbers returned by get_stop_numbers"""
        stop_nums = self.p_stops.get_stop_numbers()
        assert stop_nums == ["1", "1", "1"]

    def test_lap_numbers(self):
        """Test the lap numbers returned by get_lap_numbers"""
        lap_nums = self.p_stops.get_lap_numbers()
        assert lap_nums == ["1", "1", "12"]

    def test_times(self):
        """Test the times returned by get_times"""
        r_times = self.p_stops.get_times()
        assert r_times == ["16:15:28", "16:15:30", "16:31:50"]

    def test_durations(self):
        """Test the pitstop durations returned by get_durations()"""
        positions = self.p_stops.get_durations()
        assert positions == ["32.997", "33.027", "23.299"]
