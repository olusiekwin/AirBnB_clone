#!/usr/bin/python3
"""
Unit Tests for BaseModel Class - Unified Implementation
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_init(self):
        """
        Test for the correct initialization of attributes
        """
        cls = BaseModel()
        self.assertIsNotNone(cls.id)
        self.assertIsInstance(cls.created_at, datetime)
        self.assertIsInstance(cls.updated_at, datetime)

    def test_str(self):
        """
        Test for __str__ to return the correct format
        """
        cls = BaseModel()
        string = str(cls)
        self.assertIn('[BaseModel', string)
        self.assertIn(cls.id, string)

    def test_save(self):
        """
        Test for the save function to compare time on updated_at
        """
        cls = BaseModel()
        last_updated_at = cls.updated_at
        cls.save()
        self.assertLess(last_updated_at, cls.updated_at)

    def test_created_at_save(self):
        """
        Test for the save function to compare created_at
        """
        cls = BaseModel()
        last_created_at = cls.created_at
        cls.save()
        self.assertEqual(last_created_at, cls.created_at)

    def test_id_save(self):
        """
        Test for save method to save the id
        """
        cls = BaseModel()
        c_id = cls.id
        cls.save()
        self.assertEqual(c_id, cls.id)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        cls = BaseModel()
        cls_dict = cls.to_dict()
        self.assertIsInstance(cls_dict, dict)


if __name__ == '__main__':
    unittest.main()
