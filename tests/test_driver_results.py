'''This module is responsible for testing the methods in driver_results.py'''

import json
from f1pystats.driver_results import DriverResults


class TestDriverResults:
    '''Contains functions for testing the methods in DriverResults'''

    data = ""
    with open("tests/top_3_2008.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    d_res = DriverResults(data)

    def test_driver_positions(self):
        '''Test the positions returned by get_driver_positions'''
        driver_pos = self.d_res.get_driver_positions()
        assert driver_pos == ["1", "2", "3"]

    def test_driver_names(self):
        '''Test the names returned by get_driver_names'''
        driver_names = self.d_res.get_driver_names()
        assert driver_names == ["Lewis Hamilton",
                                "Felipe Massa",
                                "Kimi Räikkönen"]

    def test_driver_points(self):
        '''Test the points returned by get_driver_points'''
        driver_points = self.d_res.get_driver_points()
        assert driver_points == ["98", "97", "75"]

    def test_driver_teams(self):
        '''Test the teams returned by get_driver_teams'''
        driver_teams = self.d_res.get_driver_teams()
        assert driver_teams == ["McLaren",
                                "Ferrari",
                                "Ferrari"]

    def test_driver_nationality(self):
        '''Test the nationalities returned by get_driver_nationalities'''
        driver_nationalities = self.d_res.get_driver_nationality()
        assert driver_nationalities == ["British",
                                        "Brazilian",
                                        "Finnish"]

    def test_driver_wins(self):
        '''Test the number of wins returned by get_driver_wins'''
        driver_wins = self.d_res.get_driver_wins()
        assert driver_wins == ["5", "6", "2"]
