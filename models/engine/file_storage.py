#!/usr/bin/python3
"""recreate a BaseModel from another
one by using a dictionary representation"""
import json


class FileStorage():

    def __init__(self):

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json_file.write(json.dumps(self.__objects))

    def reload(self):
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.loads(json_file.read())
        except Exception:
            pass
