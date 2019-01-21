#!/usr/bin/python

from .Manager import Manager
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
import csv


class Fridge(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()
        with open('data/mock/fridge.csv', newline='') as file:
            """File is formatted:
            Alcoholic
            Name,Price,Description, Alcohol%,Package,Category
            ...
            ...
            ...
            NonAlcoholic
            Name,Price,Description, Carbonated,Sugar Content,Package,Caffiene Content
            ...
            ...
            ...        
            """
            self.parse(file)

    def parse(self, file):
        """Will be implemented in A2, will parse inventory data when adding to Inventory fridge"""
        # skip header line
        d_id = 0
        line = file.readline().strip()
        if line == 'Alcoholic':
            next(file)
            fp = csv.reader(file)

            for row in fp:
                if row[0] == 'NonAlcoholic':
                    line = row[0]
                    break

                drink = Alcoholic(d_id, row[0], int(row[1]), row[2], int(row[3]), row[4], row[5])
                self.add_drink(drink)
                d_id += 1
        if line == 'NonAlcoholic':
            next(file)
            fp = csv.reader(file)

            for row in fp:
                is_carbonated = True
                if row[3] == 'False':
                    is_carbonated = False

                drink = NonAlcoholic(d_id, row[0], int(row[1]), row[2], is_carbonated, row[4], row[5], row[6])
                self.add_drink(drink)
                d_id += 1
