#!/usr/bin/python3
"""This is the first step towards building your first full web application:
   the AirBnB clone. This first step is very important because you will use
   what you build during this project with all other following projects: H
   HTML/CSS templating, database storage, API, front-end integration"""

import datetime
import uuid
import models


class BaseModel():
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kargs):
        """constractor"""
        if len(kargs) > 0:
            for key, value in kargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return a string representation of the class"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """modifies the updated_at attr"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """retrun a modified dict"""
        cp_dict = self.__dict__.copy()
        cp_dict['created_at'] = self.created_at.isoformat()
        cp_dict['updated_at'] = self.updated_at.isoformat()
        cp_dict['__class__'] = self.__class__.__name__
        return cp_dict
