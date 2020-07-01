#!/usr/bin/python3
"""Module to define the user Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class User(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor for class User
        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object
        """
        super().__init__()
