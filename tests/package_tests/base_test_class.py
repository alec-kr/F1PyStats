"""This is the base class for all package test modules"""


class BaseTestClass:
    """These class methods are used to test the functions in f1pystats"""
    # pylint: disable=import-outside-toplevel
    import json
    import pytest
    import f1pystats.f1pystats as fp
    # pylint: enable=import-outside-toplevel

    def get_vals(self, json_data):
        """Convert the API's JSON values into a nested list"""
        return json_data.values.tolist()

    def get_data(self, file_name):
        """Read and store the data in the test data files"""
        data = ""
        with open(f"tests/test_data/api_data/{file_name}", encoding="utf-8") as data_file:
            data = self.json.load(data_file)

        return data
