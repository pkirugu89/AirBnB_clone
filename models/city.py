#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes City class attributes.
        Attributes:
            state_id (str): ID of state.
            name (str): name of the state.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
