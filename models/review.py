#!/usr/bin/python3
"""
Review class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Child class with the following public class attributes:

    Public attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize args and kwargs

        Args:
            args: will not be used
            kwargs: keyword args
        """
        super().__init__(*args, **kwargs)
