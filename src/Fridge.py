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
        except FileNotFoundError:
            print("State of Fridge not found")

        try:
            with open('data/mock/nonalcoholic.csv', newline='') as file:
                """File is formatted:
                Name,Price,Description,Carbonated,Sugar Content,Package,Caffeine Content
                ...
                ...
                ...
                """
                self.add(file)
        except FileNotFoundError:
            print("Non Alcoholic Mock File missing")
        except IndexError:
            print("Non Alcoholic Mock Import failed")

    #Pre: File must be a valid file location
    #Post: Loads binary object information from file and saves into dictionary of drinks object if not NonAlcoholic beverage
    def parse(self, file):
        """Parses Fridge data from serialized object using pickle."""
        self.drinks = pickle.load(file)
        for drink in self.drinks:
            if isinstance(drink, NonAlcoholic) and drink.selected == False:
                self.remove_drink(drink.id)

    #Pre: None
    #Post: Saves dictionary of drinks to binary file
    def save(self):
        bin = open('data/fridge.bin', mode="wb")
        pickle.dump(self.drinks, bin)
        bin.close()


    #Pre: File must be a valid file location and must contain only NonAlcoholic Beverages in correct format (Mock Data)
    #Post: Adds NonAlcoholic drinks to dictionary of drinks
    def add(self, file):
        d_id = -1
        next(file)
        fp = csv.reader(file)

        for row in fp:
            is_carbonated = True
            if row[3] == 'False':
                is_carbonated = False

            drink = NonAlcoholic(d_id, row[0], int(row[1]), row[2], is_carbonated, row[4], row[5], row[6])
            if not self.has_drink(drink.id):
                self.add_drink(drink)

            d_id -= 1
