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

    def test_2_serialization(self):
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

    def test_3_deserialization(self):
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

    def test_4(self):
        """Checks if correct error Rises."""
        with self.assertRaises(AttributeError):
            storage.new(None)
    
    def test_5_objects_not_empty(self):
        """checks if class attribute __objects fills after model instance"""
        my_model = BaseModel()
        my_model.name = "test_01"
        my_model.my_number = 1
        my_obj = FileStorage()
        my_obj.reload()
        all_objs = my_obj.all()

        # check if __objects is not empty
        self.assertNotEqual(all_objs, {})

        # check the correct key of the object
        my_key = str(type(my_model).__name__) + "." + str(my_model.id)
        self.assertTrue(my_key in all_objs.keys())

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        model = BaseModel()
        updated_1 = str(model.updated_at)
        model.name = "Betty"
        model.save()
        updated_2 = str(model.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        model = BaseModel()
        created_1 = str(model.created_at)
        model.last_name = "Holberton"
        model.save()
        created_2 = str(model.created_at)
        self.assertEqual(created_1, created_2)
