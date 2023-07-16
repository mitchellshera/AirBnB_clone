#!/usr/bin/python3

"""
This module contains the test cases for models.user
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains the tests for class User
    It test both default and assigned values
    """
    def setUp(self):
        """ setup for testing """
        self.user = User()

    def test_defaultValues(self):
        """ Test for default values of user attributes """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_assignedValues(self):
        """ Test for assigned values of attributes """
        self.user.email = "mymail@mail.com"
        self.user.password = "passcode"
        self.user.first_name = "Jina"
        self.user.last_name = "Pili"

        self.assertEqual(self.user.email, "mymail@mail.com")
        self.assertEqual(self.user.password, "passcode")
        self.assertEqual(self.user.first_name, "Jina")
        self.assertEqual(self.user.last_name, "Pili")


if __name__ == '__main__':
    unittest.main()
