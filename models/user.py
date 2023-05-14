#!/usr/bin/python3
"""Module user.py with class User that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines the attributes of a particular User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
