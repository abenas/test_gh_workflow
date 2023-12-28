"""
Test the `check` module.
"""

import unittest
import tempfile
import os
from src import check


class TestCheck(unittest.TestCase):
    """
    This class contains unit tests for the `check` module.
    """

    def test_has_import(self):
        """
        Test the `has_import` function with various input values.

        This test asserts that the `has_import` function returns the correct
        output for different input values.
        """
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"import os\n")
            f.write(b"import sys\n")
            f.write(b"from math import sqrt\n")
            temp_filename = f.name

        self.assertTrue(check.has_import(temp_filename, 'os'))
        self.assertTrue(check.has_import(temp_filename, 'sys'))
        self.assertTrue(check.has_import(temp_filename, 'math'))
        self.assertFalse(check.has_import(temp_filename, 'numpy'))

        os.unlink(temp_filename)
