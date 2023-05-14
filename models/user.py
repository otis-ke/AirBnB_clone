#!/usr/bin/python3
""" Module amenity.py with class Amenity that inherits from BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenities offered by a User.
    Attributes:
        name (str): name of the amenity
    """
    name = ""
