#!/usr/bin/python3
"""
Module base_model.py defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the class
        Args:
            *args (any): not used
            **kwargs (dictionary): key-value pairs of attributes
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, date_format)
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints instance as: [<class name>] (<self.id>) <self.__dict__>"""
        objs = '[{}] ({}) {}'
        return objs.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        tmp_dict = self.__dict__.copy()
        tmp_dict["created_at"] = self.created_at.isoformat()
        tmp_dict["updated_at"] = self.updated_at.isoformat()
        tmp_dict["__class__"] = self.__class__.__name__
        return tmp_dict
