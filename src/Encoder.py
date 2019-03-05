#!/usr/bin/python
import json


class JSONEncoder (json.JSONEncoder):
    """JSON custom encoder to transform private variables to public property names
       (to conform to PEP8 standards of exposing only 'public variables')
       i.e. {'_name': 'Absolut Vodka'} --> {'name': 'Absolut Vodka'}"""
    #Pre: obj must be a valid object instance
    #Post: returns string representation of object attributes without sunder
    @staticmethod
    def default(obj):
        return {k.lstrip('_'): v for k, v in vars(obj).items()}

