#!/usr/bin/python3

"""
8. First User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel with the following attributes:
    email: user email
    password: user password
    first_name: user first name
    last_name: user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
