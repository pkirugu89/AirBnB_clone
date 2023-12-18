#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the class attributes.
        Attributes:
            place_id (str): id of the place.
            user_id (str): id of the user.
            text (str): user's review of the place.
        """
        super().__init__(self, *args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
