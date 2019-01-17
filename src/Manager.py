#!/usr/bin/python

from abc import ABC, abstractmethod


class Manager(ABC):
    """Abstract management class for all Drinks and method prototypes for maintaining drinks and drink information"""

    def __init__(self):
        self._drinks = {}

    @property
    def drinks(self):
        """Returns dictionary containg all drinks in the manager"""
        return self._drinks

    @abstractmethod
    def get_drink(self, _id):
        """Returns drink in dictionary based off of a given id"""
        pass

    @abstractmethod
    def add_drink(self, drink):
        """Adds a drink to the dictionary"""
        pass

    @abstractmethod
    def has_drink(self, _id, ):
        """Checks if a drink exists in the dictionary
           returns boolean indicator"""
        pass

    @abstractmethod
    def find_drink(self, attr, value):
        """Finds a drink in the dictionary based on a parameter attribute
        and returns it"""
        pass

    @abstractmethod
    def remove_drink(self, _id):
        """Removes a drink from the dictionary by id
           does not return it"""
        pass

