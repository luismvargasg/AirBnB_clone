#!/usr/bin/python3
"""recreate a BaseModel from another one by using a
dictionary representation.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """constructor to the class FileStorage"""
        pass

    def all(self):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(my_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects ONLY if the JASON file
        exists, otherwise, do nothing.  If the file doesn't exist, exceptions
        should be raised
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                json_loads = json.load(json_file)
            for key, value in json_loads.items():
                load_obj = "{}(**{})".format(value['__class__'], value)
                self.__objects[key] = eval(load_obj)
        except:
            pass

    def delete(self, key):
        """deletes an instance based on the class name and id and
        update the JSON file
        """
        del self.__objects[key]
        self.save()
