#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class attributes.
        Attributes:
            city_id (str): id of the city.
            user_id (str): id of the user.
            name (str): name of the user.
            description (str): place description.
            number_rooms (int): number of available rooms.
            number_bathrooms (int): number of bathrooms.
            max_guest (int): number of maximum guest of a place.
            price_by_night (int): price of the place per night.
            latitude (float): latitide position of the place.
            longitude (float): longitude position of the place.
            amenity_ids (dict): amenity ids of a place.
        """
        super().__init__(self, *args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
