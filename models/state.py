#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class attributes.
        Attribute:
            name (str): Name of State.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
