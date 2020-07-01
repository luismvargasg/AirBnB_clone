#!/usr/bin/python3
"""Module to define the State Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class State(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor for class State
        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object
        """
        super().__init__()
