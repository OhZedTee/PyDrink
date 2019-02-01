#!/usr/bin/python
from .Encoder import JSONEncoder
import json

class Drink:
    """Common base class for all beverages
        All Drinks have a drink ID (did), a name, cost, and description"""

    def __init__(self, did, name, cost, desc):
        self._id = did
        self._name = name
        self._cost = cost
        self._desc = desc
        self._selected = False
        self._unique_params = {}

    @property
    def id(self):
        """Unique Id of drink"""
        return self._id

    @property
    def name(self):
        """Get Name of drink"""
        return self._name

    @name.setter
    def name(self, name):
        """Set Name of drink"""
        self._name = name

    @property
    def cost(self):
        """Get Cost of drink"""
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Set Cost of drink"""
        self._cost = cost

    @property
    def desc(self):
        """Get Description of drink"""
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Set Description of drink"""
        self._desc = desc

    @property
    def selected(self):
        """Get Selected property of drink"""
        return self._selected

    @selected.setter
    def selected(self, value):
        """Set Selected property of drink"""
        self._selected = value

    @property
    def unique_params(self):
        """Get Unique Params for each drink"""
        return self._unique_params

    @unique_params.setter
    def unique_params(self, value):
        self._unique_params = value

    def get_unique_param(self, key):
        """Returns unique params in dictionary based off of a param key"""
        return self._unique_params[key]

    def add_unique_param(self, key, value):
        """Adds a unique params to the dictionary"""
        self._unique_params[key] = value

    def has_unique_param(self, key):
        """Checks if a unique params exists in the dictionary
           returns boolean indicator"""
        if key not in self._unique_params:
            return False
        return True

    def find_unique_param(self, attr, value):
        """Finds a unique params in the dictionary based on a parameter attribute
        and returns it"""
        for param in self._unique_params.values():
            if getattr(param, attr, False) == value:
                return param

    def remove_unique_param(self, key):
        """Removes a unique params from the dictionary by param key
           does not return it"""
        del self._unique_params[key]

    def clear_unique_params(self):
        """Removes all unique params from the unique params dictionary"""
        self._unique_params.clear()

    def dumps(self):
        """Dump JSON data of object"""
        return json.dumps(self, ensure_ascii=True, cls=JSONEncoder, indent=4)

    def __str__(self):
        return "Name: %s\nCost: %s\nDescription: %s\n\n\n************JSON**********\n%s"\
               % (self.name, '${:,.2f}'.format(float(self.cost)/100.), self.desc, self.dumps())
