#!/usr/bin/python3
"""
Module for testing FileStorage class behavior.
"""

import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Test the FileStorage class.
    """
    def setUp(self):
        """
        Set up the test case.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up the test case.
        """
        try:
            os.remove(FileStorage.__file_path)
        except FileNotFoundError:
            pass

    def test_file_path_exists(self):
        """
        Test if __file_path exists.
        """
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))

    def test_save_reload(self):
        """
        Test if objects are saved and reloaded correctly.
        """
        # Create some test objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()

        # Reload the storage
        self.storage.reload()

        # Check if the reloaded objects exist
        self.assertIn(obj1, self.storage.all().values())
        self.assertIn(obj2, self.storage.all().values())

    def test_save_reload_json_file(self):
        """ Test if JSON file is created, saved, and reloaded. """
        # Create a test object
        obj = BaseModel()
        obj.save()

        # Check if the JSON file exists after saving
        self.assertTrue(os.path.isfile(FileStorage.__file_path))

        # Reload the storage
        self.storage.reload()

        # Check if the object exists after reloading
        self.assertIn(obj, self.storage.all().values())

    def test_save_reload_attributes(self):
        """ Test if object attributes are correctly saved and reloaded. """
        # Create a test object with specific attributes
        obj = BaseModel()
        obj.name = "Test Object"
        obj.age = 25
        obj.save()

        # Reload the storage
        self.storage.reload()

        # Check if the attributes are correctly reloaded
        reloaded_obj = self.storage.all()[f"BaseModel.{obj.id}"]
        self.assertEqual(reloaded_obj.name, obj.name)
        self.assertEqual(reloaded_obj.age, obj.age)


if __name__ == "__main__":
    unittest.main()
