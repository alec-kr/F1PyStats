"""This module is responsible for testing the methods in finishing_status.py"""

import json

from f1pystats.finishing_status import FinishingStatus


class TestFinishingStatus:
    """Contains functions for testing the methods in FinishingStatus"""

    data = ""
    with open("tests/test_data/module_data/top_3_status_2010.json", encoding='utf-8') as f:
        data = json.load(f)

    f_status = FinishingStatus(data)

    def test_get_status_id(self):
        """Test the status id returned by get_status_id"""
        status_id = self.f_status.get_status_id()
        assert status_id == [
            "1", "3", "4"
        ]

    def test_get_status(self):
        """Test the status info returned by get_status"""
        status = self.f_status.get_status()
        assert status == [
            "Finished",
            "Accident",
            "Collision"
        ]

    def test_get_status_count(self):
        """Test the status count returned by get_status_count"""
        status_count = self.f_status.get_status_count()
        assert status_count == [
            "212",
            "17",
            "25"
        ]
