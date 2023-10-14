#!/usr/bin/python3
'''
Module
'''
import unittest
from unittest.mock import patch
from models.base_model import MyModel
from uuid import UUID
from datetime import datetime


class TestMyModel(unittest.TestCase):
    '''
    Docs
    '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("models.base_model").base_model.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        '''
        classDoc = __import__("models.base_model").base_model.MyModel.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.MyModel.my_save.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsto_dict(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.MyModel.to_my_dict.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocs__str___(self):
        '''
        '''
        methodDoc = (
                __import__("models.base_model")
                .base_model.MyModel.__my_str__.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_my_idType(self):
        '''
        '''
        obj = MyModel()
        self.assertIs(type(obj.my_id), str)

    def test_my_idLength(self):
        '''
        '''
        obj = MyModel()
        self.assertEqual(len(obj.my_id), 36)

    def test_my_idValidity(self):
        '''
        '''
        obj = MyModel()
        value = UUID(obj.my_id)
        self.assertIs(type(value), UUID)

    def test_my_created_atType(self):
        '''
        '''
        obj = MyModel()
        self.assertIs(type(obj.my_created_at), datetime)

    def test_my_updated_atType(self):
        '''
        '''
        obj = MyModel()
        self.assertIs(type(obj.my_updated_at), datetime)

    def test_outputOf__str__(self):
        '''
        '''
        obj = MyModel()
        str1 = f"[MyModel] ({obj.my_id}) {obj.__dict__}"
        str2 = str(obj)

        self.assertEqual(str1, str2)

    def test_my_updated_atChanged(self):
        '''
        '''
        obj = MyModel()
        initial_value = obj.my_updated_at
        obj.my_save()

        self.assertGreater(obj.my_updated_at, initial_value)

    def test_to_my_dictCheck(self):
        '''
        '''
        obj = MyModel()
        to_dict_dict = obj.to_my_dict()
        __dict__dict = obj.__dict__

        for keys in __dict__dict:
            self.assertIn(keys, to_dict_dict)

    def test_to_my_dict(self):
        '''
        '''
        obj = MyModel()
        to_dict_dict = obj.to_my_dict()

        self.assertIn("__class__", to_dict_dict)
        self.assertIs(type(to_dict_dict["__class__"]), str)

    def test_to_my_dict_Valid(self):
        '''
        '''
        obj = MyModel()
        to_dict_dict = obj.to_my_dict()
        created_at = datetime.fromisoformat(to_dict_dict["my_created_at"])
        updated_at = datetime.fromisoformat(to_dict_dict["my_updated_at"])

        self.assertIn("my_created_at", to_dict_dict)
        self.assertIn("my_updated_at", to_dict_dict)
        self.assertIs(type(to_dict_dict["my_created_at"]), str)
        self.assertIs(type(to_dict_dict["my_updated_at"]), str)
        self.assertEqual(to_dict_dict["my_created_at"], created_at.isoformat())
        self.assertEqual(to_dict_dict["my_updated_at"], updated_at.isoformat())

    def test_dictType(self):
        '''
        '''
        obj = MyModel()
        to_dict_dict = obj.to_my_dict()

        self.assertIs(type(to_dict_dict["my_id"]), str)


if __name__ == "__main__":
    unittest.main()
