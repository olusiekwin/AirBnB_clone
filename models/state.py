#!/usr/bin/python3
"""
State class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class with the following public attributes:

    Public attributes:
        name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize args and kwargs

        Args:
            args: Will not be used
            kwargs: Keyword args
        """
        super().__init__(*args, **kwargs)
