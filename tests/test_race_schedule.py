'''This module is responsible for testing the methods in test_race_schedule.py'''

import json
from f1pystats.race_schedule import RaceSchedule


class TestRaceSchedule:
    '''Contains functions for testing the methods in RaceSchedule'''

    data = ""
    with open("tests/test_data/first_3_races_2008.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    r_sched = RaceSchedule(data)

    def test_race_rounds(self):
        '''Test the round numbers returned by get_race_rounds'''
        race_rounds = self.r_sched.get_race_round()
        assert race_rounds == ["1", "2", "3"]

    def test_race_names(self):
        '''Test the race names returned by get_race_names'''
        race_names = self.r_sched.get_race_names()
        assert race_names == [
            "Australian Grand Prix",
            "Malaysian Grand Prix",
            "Bahrain Grand Prix"
        ]

    def test_race_dates(self):
        '''Test the dates returned by get_race_schedule_dates'''
        race_dates = self.r_sched.get_race_schedule_dates()
        assert race_dates == [
            "2008-03-16",
            "2008-03-23",
            "2008-04-06"
        ]

    def test_race_circuits(self):
        '''Test the circuit names returned by get_race_circuits'''
        race_circuits = self.r_sched.get_race_circuits()
        assert race_circuits == [
            "Albert Park Grand Prix Circuit",
            "Sepang International Circuit",
            "Bahrain International Circuit"
        ]

    def test_race_times(self):
        '''Test the race times returned by get_race_schedule_times'''
        race_times = self.r_sched.get_race_schedule_times()
        assert race_times == [
            "04:30:00Z",
            "07:00:00Z",
            "11:30:00Z"
        ]

    def test_race_countries(self):
        '''Test the host countries returned by get_race_countries'''
        race_countries = self.r_sched.get_race_countries()
        assert race_countries == [
            "Australia",
            "Malaysia",
            "Bahrain"
        ]

    def test_race_localities(self):
        '''Test the local area names returned by get_race_localities'''
        race_localities = self.r_sched.get_race_locality()
        assert race_localities == [
            "Melbourne",
            "Kuala Lumpur",
            "Sakhir"
        ]
