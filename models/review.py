#!/usr/bin/python3
"""Module to define the review Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class Review(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """review class constructor method

        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object.
        """
        super().__init__()
