#!/usr/bin/python3
"""Module to create Base model"""
from datetime import datetime
from datetime import date
import uuid 


class BaseModel:
    """ Class Base of all models"""
    def __init__(self, *args, **kwargs):
        """Constructor function,
        using arguments *Args, **kwargs"""
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(uuid.uuid1())
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, date_format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, date_format)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
    def __str__(self):
        """String representation"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    
    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['updated_at'] = self.updated_at.isoformat()
        base_dict['created_at'] = self.created_at.isoformat()
        return(base_dict)

