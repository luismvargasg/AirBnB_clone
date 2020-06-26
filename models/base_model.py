#!/usr/bin/python3
"""Module to define the BaseModel Class"""
import uuid
import datetime as dt


class BaseModel:
    """class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """Base class constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = dt.datetime.now()

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance.
        """
        myDict = self.__dict__.copy()
        myDict["__class__"] = self.__class__.__name__
        myDict["created_at"] = self.created_at.isoformat()
        myDict["updated_at"] = self.updated_at.isoformat()
        return myDict

    def __str__(self):
        """string representation of the created class.

        Return:
            format: [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
        return string
