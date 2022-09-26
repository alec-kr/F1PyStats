import json
import sys
sys.path.insert(0, '.') 
from f1pystats.driver_results import DriverResults

class TestDriverResults:
    f = open("top_3_2008.json")
    data = json.load(f)
    f.close()

    d_res = DriverResults(data)


    def test_driver_positions(self):
        driver_pos = self.d_res.get_driver_positions()
        assert driver_pos == ["1", "2", "3"]


    def test_driver_names(self):
        driver_names = self.d_res.get_driver_names()
        assert driver_names == ["Lewis Hamilton", "Felipe Massa", "Kimi Räikkönen"]
    

    def test_driver_points(self):
        driver_points = self.d_res.get_driver_points()
        assert driver_points == ["98", "97", "75"]


    def test_driver_teams(self):
        driver_teams = self.d_res.get_driver_teams()
        assert driver_teams == ["McLaren", "Ferrari", "Ferrari"]


    def test_driver_nationality(self):
        driver_nationalities = self.d_res.get_driver_nationality()
        assert driver_nationalities == ["British", "Brazilian", "Finnish"]


    def test_driver_wins(self):
        driver_wins = self.d_res.get_driver_wins()
        assert driver_wins == ["5", "6", "2"]