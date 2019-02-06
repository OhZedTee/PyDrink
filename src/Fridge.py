#!/usr/bin/python

from .Manager import Manager
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
import csv
import pickle
import sys


class Fridge(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()
        try:
            with open('data/fridge.bin', mode="rb") as file:
                self.parse(file)
            with open('data/mock/nonalcoholic.csv', newline='') as file:
                """File is formatted:
                Name,Price,Description,Carbonated,Sugar Content,Package,Caffeine Content
                ...
                ...
                ...
                """
                print("adding")
                sys.stdout.flush()
                self.add(file)
        except:
            print("State of Fridge not found")

    def parse(self, file):
        """Parses Fridge data from serialized object using pickle."""
        self.drinks = pickle.load(file)
        for drink in self.drinks:
            if isinstance(drink, NonAlcoholic):
                self.remove_drink(drink.id)


    def save(self):
        bin = open('data/fridge.bin', mode="wb")
        pickle.dump(self.drinks, bin)
        bin.close()


    def add(self, file):
        d_id = -1
        next(file)
        fp = csv.reader(file)

        for row in fp:
            is_carbonated = True
            if row[3] == 'False':
                is_carbonated = False

            drink = NonAlcoholic(d_id, row[0], int(row[1]), row[2], is_carbonated, row[4], row[5], row[6])
            self.add_drink(drink)
            d_id -= 1
