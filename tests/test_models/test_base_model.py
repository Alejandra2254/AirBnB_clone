#!/usr/bin/python3
"""Base Model Test module"""
import unittest
import uuid
import time
from datetime import datetime  # for strftime
from datetime import date
from models import storage
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Class to test the BaseModel Class"""

    def test_0__id(self):
        """using uuid, if the lenght is 36, is atring and unique"""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertEqual(len(model_1.id), 36)
        self.assertEqual(type(model_1.id), str)
        self.assertNotEqual(model_1.id, model_2.id)

    def test_1_created_at(self):
        """created_at as datetime type and equal updated"""
        model_1 = BaseModel()
        self.assertEqual(type(model_1.created_at), datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)

    def test_2_updated_at(self):
        """if update_at is datetime type and equal to created_at"""
        model_1 = BaseModel()
        self.assertEqual(type(model_1.updated_at), datetime)
        self.assertEqual(model_1.created_at, model_1.updated_at)

    def test_3_save_method(self):
        """If updated_at works when save() is called"""
        b1 = BaseModel()
        crtime = b1.created_at
        uptime = b1.updated_at
        sleep(0.1)
        b1.save()
        self.assertTrue(crtime == b1.created_at)
        self.assertFalse(uptime == crtime)
        self.assertFalse(uptime == b1.updated_at)
