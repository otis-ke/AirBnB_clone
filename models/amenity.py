<<<<<<< HEAD
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
"""Module amenity.py with class Amenity that inherits from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenities offered by a User.
    Attributes:
        name (str): name of the amenity
    """
    name = ""
>>>>>>> 6ecacbae983f5aabb6c9a32dec7a8687b856cd1f
