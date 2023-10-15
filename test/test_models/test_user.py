import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import models
import os
import time


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_child_class(self):
        """
        Test if User is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_set_attributes(self):
        """
        Test for the availability of attributes in the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_empty_attribute_strings(self):
        """
        Test for default empty attribute strings in User instances.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """
        Test the to_dict method for User instances.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_kwargs(self):
        """
        Test attribute initialization using kwargs in User instances.
        """
        user = User()
        user = User(email="r", password="x", first_name="T", last_name="mk")
        self.assertEqual(user.email, "r")
        self.assertEqual(user.password, "x")
        self.assertEqual(user.first_name, "T")
        self.assertEqual(user.last_name, "mk")

    def test_main_attributes(self):
        """
        Test that the main attributes in User instances are not empty.
        """
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of User instances.
        """
        user = User()
        string = str(user)
        self.assertIn('[User]', string)
        self.assertIn(user.id, string)

    def test_save(self):
        """
        Test the save method on User instances.
        """
        user = User()
        created_at = user.created_at
        updated_at = user.updated_at
        user.save()
        self.assertNotEqual(created_at, user.updated_at)

    def test_two_saves(self):
        """
        Test the effectivity of different timestamps after multiple saves.
        """
        user = User()
        updated_at_1 = user.updated_at
        user.save()
        updated_at_2 = user.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        time.sleep(0.1)
        user.save()
        self.assertLess(updated_at_2, user.updated_at)

    def test_save_updates_file(self):
        """
        Test that updates are correctly updated and stored in the JSON file.
        """
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as file:
            self.assertIn(user_id, file.read())

    def test_to_dict_method(self):
        """
        Test the to_dict method of User instances.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_to_dict_has_correct_keys(self):
        """
        Test that the dictionary returned by to_dict has the correct keys.
        """
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("__class__", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())

    def test_to_dict_created_at_format(self):
        """
        Test that the 'created_at' key in the dictionary has the correct
        format.
        """
        user = User()
        user_dict = user.to_dict()
        created_at = user_dict["created_at"]
        self.assertEqual(created_at, user.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """
        Test that the 'updated_at' key in the dictionary has the correct
          format.
        """
        user = User()
        user_dict = user.to_dict()
        updated_at = user_dict["updated_at"]
        self.assertEqual(updated_at, user.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
