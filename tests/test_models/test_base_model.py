#!/usr/bin/python3
"""Base Model Test module"""
import unittest
import uuid
from datetime import datetime  # for strftime
from datetime import date
from models import storage
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """Class to test the BaseModel Class"""
    
    def test_0__id(self):
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertEqual(len(model_1.id), 36)
        self.assertEqual(type(model_1.id), str)
        self.assertNotEqual(model_1.id, model_2.id)
    
    def test_1_created_at(self):
        model_1 = BaseModel()
        self.assertEqual(type(model_1.created_at), datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)
    
    def test_2_updated_at(self):
        model_1 = BaseModel()
        self.assertEqual(type(model_1.updated_at), datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)