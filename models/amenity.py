#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize Amenity class attributes.
        Attributes:
            name (str): name of amenity
        """
        super().__init__(self, *args, **kwargs)
        self.name = ""
