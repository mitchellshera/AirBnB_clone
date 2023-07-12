#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        self.storage = None

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.' + self.model.id, objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        objects = self.storage.all()
        self.assertEqual(len(objects), 2)
        self.assertIn('BaseModel.' + new_model.id, objects)

    def test_save_reload(self):
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.' + self.model.id, objects)
        reloaded_model = objects['BaseModel.' + self.model.id]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.id, self.model.id)

if __name__ == '__main__':
    unittest.main()
