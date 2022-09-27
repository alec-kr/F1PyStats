'''This module is responsible for testing the methods in lap_times.py'''

import json
from f1pystats.lap_times import LapTimes


class TestLapTimes:
    '''Contains functions for testing the methods in LapTimes'''

    data = ""
    with open("tests/test_data/sample_lap_times_2008.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    l_times = LapTimes(data)

    def test_driver_names(self):
        '''Test the driver names returned from get_driver_names'''
        driver_names = self.l_times.get_driver_names()
        assert driver_names == [
            "massa",
            "kubica",
            "raikkonen"
        ]

    def test_driver_positions(self):
        '''Test the driver positions returned from get_driver_positions'''
        positions = self.l_times.get_driver_positions()
        assert positions == [
            "1",
            "2",
            "3"
        ]

    def test_lap_time(self):
        '''Test the lap times returned from get_lap_time'''
        lap_times = self.l_times.get_lap_time()
        assert lap_times == [
            "1:36.446",
            "1:37.391",
            "1:38.458"
        ]
