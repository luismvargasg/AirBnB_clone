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
    def __init__(self):

        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
