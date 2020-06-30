#!/usr/bin/python3
"""Module to define the city Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class City(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    def __init__(self):

        super().__init__()
        self.state_id = ""
        self.name = ""
