#!/usr/bin/python3
"""user class that inherts from basemode"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
