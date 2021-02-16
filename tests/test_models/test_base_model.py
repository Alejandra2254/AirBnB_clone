#!/usr/bin/python3
"""Base Model Test module"""
import unittest
import uuid
from models import storage
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """Class to test the BaseModel Class"""
    
    def test_0_leng_id(self):
        model_1 = BaseModel()
        self.assertEqual(len(model_1.id), 36)
    
    def test_1_type_id(self):
        model_1 = BaseModel()
        self.assertEqual(type(model_1.id), str)