#!/usr/bin/python3
"""Defines unittests for models/base_model.py. """


import unittest
from datetime import datetime
import models
BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_attributes(self):
        """
        Test that the BaseModel instance has the correct attributes.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """
        Test the __str__ method of the BaseModel instance.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """
        Test the save method of the BaseModel instance.
        """
        model = BaseModel()
        model.updated_at = datetime.fromtimestamp(0)

        # Act
        model.save()

        # Assert
        self.assertNotEqual(model.updated_at, datetime.now())

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel instance.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(
            model_dict["created_at"],
            model.created_at.isoformat())
        self.assertEqual(
            model_dict["updated_at"],
            model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
