#!/usr/bin/python3
"""Module to define the place Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class Place(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = 0

    def __init__(self, *args, **kwargs):
        """place class constructor method

        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object.
        """
        super().__init__()
