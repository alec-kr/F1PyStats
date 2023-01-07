"""This module is responsible for testing the methods in race_circuits.py"""

import json

from f1pystats.race_circuits import RaceCircuits


class TestRaceCircuits:
    """Contains functions for testing the methods in RaceCircuits"""
    data = ""
    with open("tests/test_data/module_data/first_3_race_circuits.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    c_obj = RaceCircuits(data)

    def test_get_circuit_name(self):
        """Test the circuit names returned from get_circuit_name"""
        cir_names = self.c_obj.get_circuit_name()
        assert cir_names == ['Albert Park Grand Prix Circuit',
                             'Bahrain International Circuit',
                             'Circuit de Barcelona-Catalunya']

    def test_get_circuit_locality(self):
        """Test the circuit locality returned from get_circuit_locality"""
        cir_locality = self.c_obj.get_circuit_locality()
        assert cir_locality == ['Melbourne', 'Sakhir', 'Montmeló']

    def test_get_circuit_country(self):
        """Test the circuit country returned from get_circuit_country"""
        cir_country = self.c_obj.get_circuit_country()
        assert cir_country == ['Australia', 'Bahrain', 'Spain']
