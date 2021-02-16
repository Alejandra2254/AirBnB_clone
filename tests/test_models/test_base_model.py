#!/usr/bin/python3
"""Base Model Test module"""
import unittest
import uuid
from time import sleep
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
        self.assertTrue(uptime == crtime)
        self.assertFalse(uptime == b1.updated_at)
    
    def test_4_str_method(self):
        """is the string representation is wrong"""
        model_1 = BaseModel()
        model_1.save()
        str_model = "[" + str(model_1.__class__.__name__) + "] (" + \
                    str(model_1.id) + ") " + str(model_1.__dict__)
        self.assertEqual(model_1.__str__(), str_model)

    def test_5_dict_method(self):
        model_1 = BaseModel()
        model_1.name = "Alejandra"
        model_1.number = 89
        my_model_dict = model_1.to_dict()
        
        #checks it is a type dictionary
        self.assertEqual(type(my_model_dict), dict)

        #check ISOFORMAT
        date_model1 = model_1.created_at
        str_date = date_model1.strftime("%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(my_model_dict['created_at'], str_date)

        #check other key
        self.assertEqual(model_1.name, my_model_dict['name'])
    
    def test_6_kwargs(self):
        """If the value is correct created with kwargs"""
        model_id = str(uuid.uuid4())
        model_1 = BaseModel(id = model_id)
        self.assertTrue(isinstance(model_1, BaseModel))
        self.assertEqual(model_id, model_1.id)