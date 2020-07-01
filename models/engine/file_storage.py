#!/usr/bin/python3
"""recreate a BaseModel from another one by using a
dictionary representation.
"""
import json


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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """deserializes the JSON file to __objects ONLY if the JASON file
        exists, otherwise, do nothing.  If the file doesn't exist, exceptions
        should be raised
        """
        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                json_load = json.load(json_file)
            for keys, values in json_load.items():
                FileStorage.__objects[k] = BaseModel(**values)
        except:
            pass

    def delete(self, key):
        """deletes an instance based on the class name and id and
        update the JSON file
        """
        del FileStorage.__objects[key]
        FileStorage.save()
