#!/usr/bin/python3
"""Module to create dile atorage"""


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        