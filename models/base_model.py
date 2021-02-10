#!/usr/bin/python3
"""Module to create Base model"""
from datetime import datetime
from datetime import date
import uuid 


class BaseModel:
    """ Class Base of all models"""
    def __init__(self):
        """Constructor function"""
        self.id = str(uuid.uuid1())
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__():
        """String representation"""
        

u = BaseModel()
print (u.id)
print (u.created_at)