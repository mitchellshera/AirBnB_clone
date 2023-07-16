#!/usr/bin/python3

"""
This module contains the test cases for models.city
"""

import models
import unittest
from models.city import City
from models.base_model import BaseModel


class test_city(unittest.TestCase):
    """
    This class contains the test cases for City
    """
    def setUp(self):
        """ Set up for city class testing """
        self.city = City()

    def test_state_id(self):
        """ Test for state id input"""
        self.assertEqual(self.city.state_id, "")

        self.city.state_id = "456"
        self.assertEqual(self.city.state_id, "456")

    def test_name(self):
        """ Test for name input"""
        self.assertEqual(self.city.name, "")

        self.city.name = "My Name"
        self.assertEqual(self.city.name, "My Name")


if __name__ == '__main__':
    unittest.main()
