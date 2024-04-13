#!/usr/bin/python3
"""This is the first step towards building your first full web application:
   the AirBnB clone. This first step is very important because you will use
   what you build during this project with all other following projects: H
   HTML/CSS templating, database storage, API, front-end integration"""

import datetime
import uuid


class BaseModel():
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """constractor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return a string representation of the class"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """modifies the updated_at attr"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """retrun a modified dict"""
        cp_dict = self.__dict__.copy()
        cp_dict['created_at'] = self.created_at.isoformat()
        cp_dict['updated_at'] = self.updated_at.isoformat()
        cp_dict['__class__'] = self.__class__.__name__
        return cp_dict
