#!/usr/bin/python3
"""
Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    Public attributes:
        name (str): An empty string
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the Amenity instance.
        Args:
            args: Not used
            kwargs: A dictionary to hold key-value arguments
        """
        super().__init__(*args, **kwargs)
        self.name = ""
