#!/usr/bin/python3
""" unittest for file sotrage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Create a fresh FileStorage instance for each test."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def test_initialization(self):
        """Test initialization of FileStorage."""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new(self):
        """Test adding new objects to storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test saving objects to JSON file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        
        with open(self.storage._FileStorage__file_path, 'r') as f:
            contents = f.read()
            self.assertIn(obj.id, contents)

    def test_reload(self):
        """Test reloading objects from JSON file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, new_storage._FileStorage__objects)
        self.assertIsInstance(new_storage._FileStorage__objects[key], BaseModel)

   def test_all(self):
    """Test the all() method returns the correct dictionary of objects."""
    obj1 = BaseModel()
    obj2 = BaseModel()
    self.storage.new(obj1)
    self.storage.new(obj2)
    all_objects = self.storage.all()
    self.assertIsInstance(all_objects, dict)
    self.assertEqual(len(all_objects), 2)
    self.assertIn(f"BaseModel.{obj1.id}", all_objects)
    self.assertIn(f"BaseModel.{obj2.id}", all_objects)


if __name__ == '__main__':
    unittest.main()
