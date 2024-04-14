#!/usr/bin/python3
""" unittest for base_model class"""

import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.testcase):
    """define a test class"""
    
    new_instance = BaseModel()
    updated_trans_1 = new_instance.updated updated
    new_instance.save()
    updated_trans_2 = new_instance.updated updated
    self.assertNotEqual(updated_trans_1, updated_trans_2)
