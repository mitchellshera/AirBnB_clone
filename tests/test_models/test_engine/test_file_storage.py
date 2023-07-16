#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.models = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }
        for model_name, model in self.models.items():
            instance = model()
            key = "{}.{}".format(model_name, instance.id)
            self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
            
    def tearDown(self):
        self.storage = None

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), len(self.models))
        for model in self.models.values():
            key = "{}.{}".format(model.__name__, list(objects.keys())[0].split(".")[1])
            self.assertIn(key, objects)

    def test_new(self):
        new_instance = Amenity()
        self.storage.new(new_instance)
        objects = self.storage.all()
        self.assertEqual(len(objects), len(self.models) + 1)
        key = "{}.{}".format(new_instance.__class__.__name__, new_instance.id)
        self.assertIn(key, objects)

    def test_save_reload(self):
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), len(self.models))
        for model in self.models.values():
            key = "{}.{}".format(model.__name__, list(objects.keys())[0].split(".")[1])
            self.assertIn(key, objects)
            self.assertIsInstance(objects[key], model)

if __name__ == '__main__':
    unittest.main()
