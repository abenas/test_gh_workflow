"""
This module contains unit tests for the `fibo` module.

The tests cover the main function in the `fibo` module, `fibonacci(n)`.
Each test checks that the `fibonacci` function returns the correct sequence for
different input values.

Example:
    Run this test module with the command `python -m unittest test_fibo.py`
"""

import unittest
from src import fibo


class TestFibo(unittest.TestCase):
    """
    This class contains unit tests for the `fibonacci` function in the `fibo`
    module.
    """

    def test_fibonacci(self):
        """
        Test the `fibonacci` function with various input values.

        This test asserts that the `fibonacci` function returns the correct
        output for different input values.
        """
        self.assertEqual(fibo.fibonacci(1), [0])
        self.assertEqual(fibo.fibonacci(2), [0, 1])
        self.assertEqual(fibo.fibonacci(3), [0, 1, 1])
        self.assertEqual(fibo.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibo.fibonacci(0), [])
        self.assertEqual(fibo.fibonacci(-1), [])
