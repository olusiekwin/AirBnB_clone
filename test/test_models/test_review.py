#!/usr/bin/python3
"""
Unit tests for the Review class
"""

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class
    """

    def setUp(self):
        """
        Set up the environment before each test case
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up the test environment after each test case if needed
        """
        self.review = None

    def test_child_class(self):
        """
        Test if Review is a child class of BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute(self):
        """
        Test for the existence of its attributes
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_empty_string(self):
        """
        Test for empty string attributes
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """
        Test converting Review class to a dictionary
        """
        state_dict = self.review.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_str(self):
        """
        Test the string representation of the Review class
        """
        string = str(self.review)
        self.assertIn('[Review]', string)

    def test_save(self):
        """
        Test if the 'save' method updates the timestamp
        """
        orig_time = self.review.created_at
        upd_time = self.review.updated_at
        self.review.save()
        self.assertTrue(orig_time != self.review.created_at)
        self.assertTrue(upd_time != self.review.updated_at)

    def test_save_updates_file(self):
        """
        Test if updates are correctly saved to the file
        """
        self.review.save()
        rvid = "Review." + self.review.id
        with open("file.json", "r") as file:
            self.assertIn(rvid, file.read())

    def test_to_dict(self):
        """
        Test if the 'to_dict' method returns the expected dictionary
        """
        expected_dict = {
            'id': self.review.id,
            'created_at': self.review.created_at.isoformat(),
            'updated_at': self.review.updated_at.isoformat(),
            '__class__': 'Review'
        }
        self.assertEqual(self.review.to_dict(), expected_dict)

    def test_to_dict_type(self):
        """
        Verify that the class returns a dictionary
        """
        self.assertTrue(isinstance(self.review.to_dict(), dict))

    def test_different_to_dict(self):
        """
        Test that different instances produce different dictionaries
        """
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertNotEqual(review1.to_dict(), review2.to_dict())

    def test_to_dict_has_correct_keys(self):
        """
        Test if the dictionary contains the correct keys
        """
        review_dict = self.review.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)

    def test_to_dict_created_at_format(self):
        """
        Check the format of the 'created_at' field in the dictionary
        """
        review_dict = self.review.to_dict()
        created_at = review_dict["created_at"]
        self.assertEqual(created_at, self.review.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """
        Check the format of the 'updated_at' field in the dictionary
        """
        review_dict = self.review.to_dict()
        updated_at = review_dict["updated_at"]
        self.assertEqual(updated_at, self.review.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
