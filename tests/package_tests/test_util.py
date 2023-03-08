"""This module contains tests for the utility functions"""

from .base_test_class import BaseTestClass


class TestUtil(BaseTestClass):
    """Tests for the utility functions"""

    def test_conv_sec(self) -> None:
        """Test seconds returned from _conv_sec"""
        assert self.fp._conv_sec("58.79") == 58.79       # N.Lauda 1974 R9 Q
        assert self.fp._conv_sec("1") == 1               # Minimum format
        want = (1 * 3600) + (23 * 60) + 45.678
        assert self.fp._conv_sec("1:23:45.678") == want  # Full format
        assert self.fp._conv_sec("") == 0                # non input
        assert self.fp._conv_sec(".") == 0               # naked decimal point
