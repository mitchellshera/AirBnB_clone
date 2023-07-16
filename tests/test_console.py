#!/usr/bin/python3


import unittest
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = console.HBNBCommand()

    def tearDown(self):
        pass

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            expected_output = "Print the string representation of an instance\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            expected_output = "** class name missing **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(f.getvalue(), expected_output)

    def test_create_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertTrue(obj_id)

    # Add more test cases for other commands


if __name__ == '__main__':
    unittest.main()
