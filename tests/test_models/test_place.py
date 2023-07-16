#!/usr/bin/python3

"""
This module contains the test cases for the file models/place
"""

import unittest
import models
from models.place import Place


class test_place(unittest.TestCase):
    """
    This class contains the test definition for place
    """

    def setUp(self):
        """ This sets up self.place """
        self.place = Place()

    def test_default_values(self):
        """ Test the default values of input in place file """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, "")
        self.assertEqual(self.place.number_bathrooms, "")
        self.assertEqual(self.place.max_guest, "")
        self.assertEqual(self.place.latitude, "")
        self.assertEqual(self.place.longitude, "")
        self.assertEqual(self.place.price_by_night, "")
        self.assertEqual(self.place.amenity_ids, "")

    def test_place_with_values(self):
        """ Test if the input values are stored correctly """
        self.place.city_id = "243"
        self.place.user_id = "675"
        self.place.name = "Nice Place"
        self.place.description = "Great view"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 120
        self.place.latitude = 34.87
        self.place.longitude = 500.64
        self.place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(self.place.city_id, "243")
        self.assertEqual(self.place.user_id, "675")
        self.assertEqual(self.place.name, "Nice Place")
        self.assertEqual(self.place.description, "Great view")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 120)
        self.assertEqual(self.place.longitude, 500.64)
        self.assertEqual(self.place.latitude, 34.87)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
