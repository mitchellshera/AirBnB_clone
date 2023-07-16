#!/usr/bin/python3

"""
This module contains the tests for the file models.state
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    This class contains the tests for State class
    It tests both default and assigned values
    """
    def setUp(self):
        """ Setting up State for testing """
        self.state = State()

    def test_name(self):
        """ Test name input """
        self.assertEqual(self.state.name, "")

        self.state.name = "Wisconsin"
        self.assertEqual(self.state.name, "Wisconsin")


if __name__ == '__main__':
    unittest.main()
