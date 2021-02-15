#!/usr/bin/python3
"""Module to crate the User Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel"""
    state_id = ""
    name = ""