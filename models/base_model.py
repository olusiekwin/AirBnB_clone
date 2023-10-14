#!/usr/bin/python3
"""
BaseModel - Unified Implementation
"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes public instance attributes.

        Args:
            args: Not used
            kwargs: A dictionary to hold key-value arguments

        Public instance attributes:
            id: Assigns a unique ID to each instance created using uuid4
            created_at: Assigns current datetime when an instance is created
            updated_at: current datetime when an instance is created or updated
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['updated_at', 'created_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'
                                                  )
                    setattr(self, key, value)
        if self.id not in storage.all():
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current time.
        """
        now = datetime.now()
        self.updated_at = now.isoformat()
        self.updated_at = datetime.strptime(self.updated_at,
                                            '%Y-%m-%dT%H:%M:%S.%f')
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all key-values of __dict__ of the instance.
        """

        dictionary = self.__dict__.copy()

        for key, value in dictionary.items():
            if key in ['updated_at', 'created_at']:
                value = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            dictionary[key] = value

        return {'__class__': type(self).__name__, **dictionary}
