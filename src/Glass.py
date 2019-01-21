#!/usr/bin/python

from .Manager import Manager
import csv


class Glass(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user is planning on using for cocktails"""
    _cocktails = {}

    def __init__(self):
        super().__init__()
        with open('data/cocktails.csv', newline='') as file:
            # skip header line
            next(file)
            fp = csv.reader(file)
            self.parse(fp)

    def parse(self, fp):
        """Parse cocktail file trying to grab elements
           (csv not made very well some aspects missing,
           therefore try catches)"""
        c_id = 0
        for row in fp:
            c = Cocktail()
            # name
            try:
                c.name = row[0]
            except IndexError:
                c.name = ''
            # glass
            try:
                c.glass = row[1]
            except IndexError:
                c.glass = ''
            # main
            try:
                c.main_alcohol = row[2]
            except IndexError:
                c.main_alcohol = ''
            # other
            try:
                c.other_alcohols = row[3]
            except IndexError:
                c.other_alcohols = ''
            # mixes
            try:
                c.mixes = row[4]
            except IndexError:
                c.mixes = ''
            # garnish
            try:
                c.garnish = row[5]
            except IndexError:
                c.garnish = ''

            self.cocktails[c_id] = c
            c_id += 1
        pass

    @property
    def cocktails(self):
        """Get list of all cocktails parsed from data"""
        return self._cocktails

    def get_cocktail(self, name):
        """Find cocktail by name and return cocktail object"""
        for cocktail in self.cocktails.values():
            if getattr(cocktail, 'name', False) == name:
                return cocktail

    def find_cocktails(self, categories):
        """Find cocktails that meet all category requirements -
               only cocktails whose main_alcohol, other_alcohols, and mixes
               are in the categories list (list of drinks in fridge)"""
        result = []
        for cocktail in self.cocktails.values():
            has_main_alcohol = False
            has_other_alcohol = False
            has_mix = False
            main_alcohol = getattr(cocktail, 'main_alcohol', False).lower()
            other_alcohol = getattr(cocktail, 'other_alcohols', False).lower()
            mixes = getattr(cocktail, 'mixes', False).lower()

            if main_alcohol == '':
                has_main_alcohol = True
            elif other_alcohol == '':
                has_other_alcohol = True
            elif mixes == '':
                has_mix = True

            for attribute in categories["Alcoholic"]:
                if attribute.lower() in main_alcohol:
                    has_main_alcohol = True
                if attribute.lower() in other_alcohol:
                    has_other_alcohol = True

            for attribute in categories["NonAlcoholic"]:
                if attribute.lower() in mixes:
                    has_mix = True

            if cocktail not in result and has_main_alcohol and has_other_alcohol and has_mix:
                result.append(cocktail)

        return result


class Cocktail:
    """Class containing all cocktail requirements: main-alcohol, other alcohols, mixes, and garnishes."""

    def __init__(self, name='', glass='', main_alcohol='', other_alcohols='', mixes='', garnish=''):
        self._name = name
        self._glass = glass
        self._main_alcohol = main_alcohol
        self._other_alcohols = other_alcohols
        self._mixes = mixes
        self._garnish = garnish

    @property
    def name(self):
        """Get Name of cocktail"""
        return self._name

    @name.setter
    def name(self, name):
        """Set Name of cocktail"""
        self._name = name

    @property
    def glass(self):
        """Get Glass type of cocktail"""
        return self._glass

    @glass.setter
    def glass(self, glass):
        """Set Glass type of cocktail"""
        self._glass = glass

    @property
    def main_alcohol(self):
        """Get main alcohol needed for cocktail"""
        return self._main_alcohol

    @main_alcohol.setter
    def main_alcohol(self, main_alcohol):
        """Set main alcohol needed for cocktail"""
        self._main_alcohol = main_alcohol

    @property
    def other_alcohols(self):
        """Get other alcohols needed for cocktail"""
        return self._other_alcohols

    @other_alcohols.setter
    def other_alcohols(self, other_alcohols):
        """Set other alcohols needed for cocktail"""
        self._other_alcohols = other_alcohols

    @property
    def mixes(self):
        """Get mixes needed for cocktail"""
        return self._mixes

    @mixes.setter
    def mixes(self, mixes):
        """Set mixes needed for cocktail"""
        self._mixes = mixes

    @property
    def garnish(self):
        """Get garnish needed for cocktail"""
        return self._garnish

    @garnish.setter
    def garnish(self, garnish):
        """Set garnish needed for cocktail"""
        self._garnish = garnish

    def __str__(self):
        return "Glass: %s\nMain Alcohol: %s\nOther Alcohols: %s\nMixes: %s\nGarnish: %s\n" % \
               (self.glass, self.main_alcohol, self.other_alcohols, self.mixes, self.garnish)

