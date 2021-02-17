#!/usr/bin/python3
"""Base Model Test module"""
import unittest
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Testfilestorage(unittest.TestCase):
    """Class to test file storage class"""

    def test_0_all_method(self):
        """Test if method all is dict"""
        dict_objects = storage.all()
        self.assertEqual(type(dict_objects), dict)

    def test_1_create_new_method(self):
        """Test to create a new method and save it"""
        my_model = BaseModel()
        my_model.name = "Valeria"
        my_model.number = 90
        my_model.save()
        all_objects = storage.all()

        self.assertNotEqual(all_objects, {})
        my_key = str(type(my_model).__name__) + "." + str(my_model.id)
        self.assertTrue(my_key in all_objects.keys())

    def test_02_serialization(self):
        """checks the correct serialization of an object"""
        my_model = BaseModel()
        my_model.name = "test_02"
        my_model.my_number = 2
        my_model.save()

        my_key = str(type(my_model).__name__) + "." + str(my_model.id)

        json_file = "file.json"  # storage.__file_path
        with open(json_file, "r", encoding='utf-8') as f:
            json_dict = json.load(f)

        exp_dict = json_dict[my_key]
        self.assertEqual(my_model.to_dict(), exp_dict)

    def test_03_deserialization(self):
        '''checks the correct deserialization of an object'''

        # this test depends on test_02_serialization
        # the json file must be present in the directory
        my_obj = FileStorage()
        my_obj.reload()  # here happens the deserialization
        all_objs = my_obj.all()
        test_obj = list(all_objs.values())[0]
        my_key = str(type(test_obj).__name__) + "." + str(test_obj.id)

        json_file = "file.json"  # storage.__file_path
        with open(json_file, "r", encoding='utf-8') as f:
            json_dict = json.load(f)
        exp_dict = json_dict[my_key]

        self.assertEqual(test_obj.to_dict(), exp_dict)

    def test_04(self):
        """Checks if correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new(None)