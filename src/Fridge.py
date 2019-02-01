#!/usr/bin/python

from .Manager import Manager
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
import csv
import pickle


class Fridge(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()
        try:
            with open('data/fridge.bin', mode="rb") as file:
                self.parse(file)
        except:
            print("State of Fridge not found")

    def parse(self, file):
        """Parses Fridge data from serialized object using pickle."""
        self.drinks = pickle.load(file)

    def save(self):
        bin = open('data/fridge.bin', mode="wb")
        pickle.dump(self.drinks, bin)
        bin.close()
