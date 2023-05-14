#!/usr/bin/python3
"""
Module file_storage.py that serializes instances to a JSON file and
deserializes JSON file to instances
"""

import json


class FileStorage:
    """Defines the FileStorage class that serializes instances to a JSON file
     and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w") as fdump:
            tmp_dict = {}
            tmp_dict.update(self.__objects)
            for key, value in tmp_dict.items():
                tmp_dict[key] = value.to_dict()
            json.dump(tmp_dict, fdump)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
         (__file_path) exists; otherwise, do nothing.
        """
        # defer the import of BaseModel to only when it is needed to prevent
        # circular imports error
        
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(self.__file_path) as fload:
                obj_dict = json.load(fload)
                for item in obj_dict.values():
                        cls_name = item["__class__"]
                        del item["__class__"]
                        self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
