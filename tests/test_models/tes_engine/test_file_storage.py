#!/usr/bin/python3
"""Base Model Test module"""
import unittest
from models import storage
from models.base_model import BaseModel

class Testfilestorage(unittest.TestCase):
    """Class to test file storage class"""

    def test_0_all_method(self):

        dict_objects = storage.all()
        self.assertEqual(type(dict_objects), dict)
    
    def test_1_create_new_method(self):

        my_model = BaseModel()
        my_model.name = "Valeria"
        my_model.number = 90
        my_model.save()
        all_objects = storage.all()

        self.assertNotEqual(all_objects, {})


        
