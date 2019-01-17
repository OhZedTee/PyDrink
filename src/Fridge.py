#!/usr/bin/python

from .Drink import Drink
from .Manager import Manager


class Fridge(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()

    def get_drink(self, _id):
        """Returns drink from Manager dictionary based off of a given id"""
        return self.drinks[str(_id)]

    def has_drink(self, _id):
        """Checks if a drink exists in the Manager dictionary
           returns boolean indicator"""
        if str(_id) not in self.drinks:
            return False
        return True

    def find_drink(self, attr, value):
        """Finds a drink in the Manager dictionary based on a parameter attribute
           and returns it"""
        for drink in self.drinks.values():
            if getattr(drink, attr, False) == value:
                return drink

    def add_drink(self, drink):
        """Adds a drink to the Manager dictionary"""
        if isinstance(drink, Drink):
            self.drinks[str(drink.id)] = drink

    def remove_drink(self, _id):
        """Removes a drink from the Manager dictionary by id
           does not return it"""
        del self.drinks[str(_id)]
