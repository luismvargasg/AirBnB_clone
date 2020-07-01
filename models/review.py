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
    def __init__(self):

        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
