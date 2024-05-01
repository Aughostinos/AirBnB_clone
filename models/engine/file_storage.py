#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import user
import os

class FileStorage():
    """serializes instances to a JSON file and deserializes 
    JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """  returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(dict_obj, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                dict_obj = json.load(file)
            for key, val in dict_obj.items():
                class_name = val['__class__']
                cls = globals()[class_name]
                obj = cls(**val)
                self.__objects[key] = obj
