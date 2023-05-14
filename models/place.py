#!/usr/bin/python3
"""Module place.py with class Place that inherits from BaseModel."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the attributes of a particular Place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
