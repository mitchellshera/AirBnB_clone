import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        # Delete the file.json if it exists after each test
        if os.path.exists(self.storage.file_path):
            os.remove(self.storage.file_path)

    def test_all(self):
        # Test if the initial 'all' method returns an empty dictionary
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

        # Test if the 'new' method adds an object to the dictionary
        model = BaseModel()
        self.storage.new(model)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(model.__class__.__name__ + '.' + model.id, objects)

    def test_new(self):
        # Test if the 'new' method adds an object to the dictionary
        model = BaseModel()
        self.storage.new(model)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(model.__class__.__name__ + '.' + model.id, objects)

    def test_save(self):
        # Test if the 'save' method serializes objects to the file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Check if the file exists
        self.assertTrue(os.path.exists(self.storage.file_path))

        # Load the file and check if the serialized object is present
        with open(self.storage.file_path, 'r') as f:
            data = json.load(f)
            key = model.__class__.__name__ + '.' + model.id
            self.assertIn(key, data)

    def test_reload(self):
        # Test if the 'reload' method deserializes objects from the file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Clear the objects dictionary
        self.storage.__objects = {}

        # Test if the 'reload' method adds the deserialized object to the dictionary
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(model.__class__.__name__ + '.' + model.id, objects)

if __name__ == '__main__':
    unittest.main()
