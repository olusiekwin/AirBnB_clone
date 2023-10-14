#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
"""
Unit  city class
"""


class TestCity(unittest.TestCase):
    """
    Test cases for City class.
    """

    def test_is_subclass(self):
        """
        Test if City is a subclass of BaseModel.
        """
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Test City attributes.
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_empty_string_attributes(self):
        """
        Test City attributes are empty strings by default.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        """
        Test to_dict method of City.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_str_method(self):
        """
        Test the str method of City.
        """
        city = City()
        city_str = str(city)
        self.assertIn("[City]", city_str)
        self.assertIn("id", city_str)
        self.assertIn("created_at", city_str)
        self.assertIn("updated_at", city_str)

    def test_save(self):
        """
        Test the save method of City.
        """
        city = City()
        orig_created_at = city.created_at
        orig_updated_at = city.updated_at
        city.save()
        self.assertEqual(orig_created_at, city.created_at)
        self.assertNotEqual(orig_updated_at, city.updated_at)

    def test_to_dict_format(self):
        """
        Test the format of to_dict output.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)
        self.assertTrue('__class__' in city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(str, type(city_dict['created_at']))
        self.assertEqual(str, type(city_dict['updated_at']))


if __name__ == '__main__':
    unittest.main()
