#!/usr/bin/python
import json


class JSONEncoder (json.JSONEncoder):
    """JSON custom encoder to transform private variables to public property names
       (to conform to PEP8 standards of exposing only 'public variables')
       i.e. {'_name': 'Absolut Vodka'} --> {'name': 'Absolut Vodka'}"""
    @staticmethod
    def default(obj):
        return {k.lstrip('_'): v for k, v in vars(obj).items()}

