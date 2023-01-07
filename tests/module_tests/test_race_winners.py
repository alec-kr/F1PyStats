"""This module is responsible for testing the methods in race_winners.py"""

import json

from f1pystats.race_winners import RaceWinners


class TestRaceWinners:
    """Contains functions for testing the methods in RaceWinners"""

    data = ""
    with open("tests/test_data/module_data/first_3_winners_2008.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    r_win = RaceWinners(data)

    def test_grands_prix(self):
        """Test the grands prix returned by get_grands_prix"""
        grands_prix = self.r_win.get_grands_prix()
        assert grands_prix == [
            "Australian Grand Prix",
            "Malaysian Grand Prix",
            "Bahrain Grand Prix",
        ]

    def test_race_winners(self):
        """Test the winner names returned by get_race_winners"""
        winners = self.r_win.get_race_winners()
        assert winners == ["Lewis Hamilton", "Kimi Räikkönen", "Felipe Massa"]

    def test_winning_constructors(self):
        """Test the constructor names returned by get_winning_constructors"""
        winners = self.r_win.get_winning_constructors()
        assert winners == ["McLaren", "Ferrari", "Ferrari"]

    def test_race_dates(self):
        """Test the race dates returned by get_race_dates"""
        race_dates = self.r_win.get_race_dates()
        assert race_dates == ["2008-03-16", "2008-03-23", "2008-04-06"]

    def test_race_laps(self):
        """Test the race laps returned by get_race_laps"""
        laps = self.r_win.get_race_laps()
        assert laps == ["58", "56", "57"]

    def test_race_times(self):
        """Test the race times returned by get_race_times"""
        race_times = self.r_win.get_race_times()
        assert race_times == ["1:34:50.616", "1:31:18.555", "1:31:06.970"]

    def test_start_position(self):
        """Test the start positions returned by get_winner_start_positions"""
        positions = self.r_win.get_winner_start_positions()
        assert positions == ["1", "2", "2"]
