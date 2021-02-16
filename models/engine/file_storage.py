#!/usr/bin/python3
"""Module to create dile atorage"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key in self.__objects.keys():
            json_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                des_dict = json.load(file)
            for key, value in des_dict.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
