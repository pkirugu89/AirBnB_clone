#!/usr/bin/python3
""" User class definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherited from BaseModel.
    Attributes:
        email (str): User email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the User class attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
