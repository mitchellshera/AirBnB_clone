#!/usr/bin/python3

"""
This module contains the test cases for amenities
"""

import models
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """
    Test cases for amenities
    """
    def setUp(self):
        """ set up for testing amenities """
        self.amenity = Amenity()
    def test_name(self):
        """ Testing the name inputs in amenities """
        pass


if __name__ == '__main__':
    unittest.main()
