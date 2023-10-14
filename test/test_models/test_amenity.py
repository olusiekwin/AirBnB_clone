import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import models


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        self.amenity = None

    def test_child_class(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute(self):
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_empty_string(self):
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        cls_dict = self.amenity.to_dict()
        self.assertIsInstance(cls_dict, dict)

    def test_str(self):
        amenity_string = str(self.amenity)
        self.assertIn('[Amenity]', amenity_string)

    def test_save(self):
        orig_time = self.amenity.created_at
        upd_time = self.amenity.updated_at
        self.amenity.save()
        self.assertEqual(orig_time, self.amenity.created_at)
        self.assertNotEqual(upd_time, self.amenity.updated_at)

    def test_id_is_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_id_is_unique(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_created_at_timestamp(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_updated_at_timestamp(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_instance_storage(self):
        self.assertIn(self.amenity, models.storage.all().values())

    def test__str__(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.__str__(), amenity2.__str__())

    def test_save_method(self):
        updated_at_1 = self.amenity.updated_at
        self.amenity.save()
        updated_at_2 = self.amenity.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_to_dict(self):
        expected_dict = {
            'id': self.amenity.id,
            'created_at': self.amenity.created_at.isoformat(),
            'updated_at': self.amenity.updated_at.isoformat(),
            '__class__': 'Amenity'
        }
        self.assertEqual(self.amenity.to_dict(), expected_dict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(self.amenity.to_dict()))

    def test_to_dict_has_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())

    def test_to_dict_created_at_format(self):
        amenity = self.amenity.to_dict()
        created_at = amenity["created_at"]
        self.assertEqual(created_at, self.amenity.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        amenity = self.amenity.to_dict()
        updated_at = amenity["updated_at"]
        self.assertEqual(updated_at, self.amenity.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
