#!/usr/bin/python

from abc import ABC, abstractmethod
from .Drink import Drink


class Manager(ABC):
    """Abstract management class for all Drinks and method prototypes for maintaining drinks and drink information"""

    def __init__(self):
        self._drinks = {}

    @property
    def drinks(self):
        """Returns dictionary containing all drinks in the manager"""
        return self._drinks

    @drinks.setter
    def drinks(self, value):
        self._drinks = value

    @abstractmethod
    def parse(self, fp):
        """Parses data to use in children classes
           i.e. Fridge will parse drinks for Manager's
           drink dictionary.
           Glass will parse cocktails for its dictionary"""
        pass

    # Pre: id must be valid integer
    # Post: Returns drink from dictionary of drinks based off id
    def get_drink(self, _id):
        """Returns drink in dictionary based off of a given id"""
        return self.drinks[str(_id)]

    # Pre: drink must be valid Drink object
    # Post: Adds drink to dictionary by id of drink object
    def add_drink(self, drink):
        """Adds a drink to the dictionary"""
        if isinstance(drink, Drink):
            self.drinks[str(drink.id)] = drink

    # Pre: id must be valid integer
    # Post: Returns True or false if id exists in dictionary
    def has_drink(self, _id):
        """Checks if a drink exists in the dictionary
           returns boolean indicator"""
        if str(_id) not in self.drinks:
            return False
        return True

    # Pre: attr must be valid string representing attribute name, value must be valid string
    # Post: Returns attribute value if found in dictionary of drinks
    def find_drink(self, attr, value):
        """Finds a drink in the dictionary based on a parameter attribute
        and returns it"""
        for drink in self.drinks.values():
            if getattr(drink, attr, False) == value:
                return drink

    # Pre: id must be valid integer
    # Post: Removes Drink object from dictionary of drinks
    def remove_drink(self, _id):
        """Removes a drink from the dictionary by id
           does not return it"""
        self.drinks[str(_id)].clear_unique_params()
        del self.drinks[str(_id)]

    # Pre: None
    # Post: Clears the dictionary of drinks
    def clear_drinks(self):
        """Removes all drinks from the Manager dictionary"""
        self.drinks.clear()
