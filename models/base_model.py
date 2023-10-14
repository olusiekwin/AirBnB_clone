#!/usr/bin/python3
'''
Module Docs:
'''
from datetime import datetime
import uuid


class MyModel:
    '''
    Class Docs
    '''

    def __init__(self):
        '''
        Docs
        '''
        self.my_id = str(uuid.uuid4())
        self.my_created_at = datetime.now()
        self.my_updated_at = self.my_created_at

    def my_save(self):
        '''
        Docs
        '''
        self.my_updated_at = datetime.now()

    def to_my_dict(self):
        '''
        Docs
        '''
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = type(self).__name__
        my_dictionary["my_created_at"] = self.my_created_at.isoformat()
        my_dictionary["my_updated_at"] = self.my_updated_at.isoformat()

        return my_dictionary

    def __my_str__(self):
        '''
        Docs
        '''
        class_name = type(self).__name__

        return "[{}] ({}) {}".format(class_name, self.my_id, self.__dict__)
