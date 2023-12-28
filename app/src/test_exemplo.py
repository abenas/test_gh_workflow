"""
This module contains the unit tests for the `exemplo` module.
"""

import unittest
from src import exemplo


class TestExemplo(unittest.TestCase):
    """
    This class contains unit tests for the `area_circle` function in the
    `exemplo`
    """

    def test_area_circle(self):
        """
        Test the `area_circle` function with various input values.

        This test asserts that the `area_circle` function returns the correct
        output for different input values.
        """
        self.assertAlmostEqual(exemplo.area_circle(0), 0)
        self.assertAlmostEqual(exemplo.area_circle(1), 3.141592653589793)
        self.assertAlmostEqual(exemplo.area_circle(2), 12.566370614359172)
