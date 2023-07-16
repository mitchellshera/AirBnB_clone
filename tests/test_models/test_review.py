#!/usr/bin/python3

"""
This module contains the test cases for the file models.review
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    This class contains the test cases fot the class Review
    It tests both default and assigned values
    """

    def setUp(self):
        """ Set up for testing review """
        self.review = Review()

    def test_Place_id(self):
        """ Test cases for place_id attribute"""
        self.assertEqual(self.review.place_id, "")

        self.review.place_id = "345"
        self.assertEqual(self.review.place_id, "345")

    def test_user_id(self):
        """ Test cases for review.user_id attribute"""
        self.assertEqual(self.review.user_id, "")

        self.review.user_id = "22"
        self.assertEqual(self.review.user_id, "22")

    def test_text(self):
        """ This tests if the review text is accepted correctly """
        self.assertEqual(self.review.text, "")

        self.review.text = "Very nice place, nice amenities"
        self.assertEqual(self.review.text, "Very nice place, nice amenities")


if __name__ == '__main__':
    unittest.main()
