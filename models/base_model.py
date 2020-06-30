#!/usr/bin/python3
"""Module to define the BaseModel Class"""
import uuid
import datetime as dt
from models import storage


class BaseModel:
    """class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Base class constructor method

        Args:
            args: Received Tuple with parameters to initialize a new object
            kwargs: Recceived Dictionary with parameters to init a new object.
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key not in ["__class__"]:
                    setattr(self, key, value)
        elif args is not None and len(args) > 0:
            attr = ["id", "created_at", "update_at", "name", "my_number"]
            for idx, value in enumerate(args):
                setattr(self, attr[idx], value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = dt.datetime.now()
        storage.new(self)
        storage.save()

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
