<<<<<<< HEAD
#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
"""Module city.py with class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines the attributes of a particular City.
    Attributes:
        state_id (str): state id
        name (str): name of the city
    """
    state_id = ""
    name = ""
>>>>>>> 6ecacbae983f5aabb6c9a32dec7a8687b856cd1f
