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


class TestFileStorage (unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
