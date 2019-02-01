#!/usr/bin/python
from .Drink import Drink
from .Encoder import JSONEncoder
import json


class Alcoholic (Drink):
    """Inherited class of Drink containing all alcoholic beverages
        All Alcoholic Beverages also have a apv (Alcohol per volume), a package type, and category"""

    def __init__(self, did, name, cost, desc, apv, package, category):
        super().__init__(did, name, cost, desc)
        self._apv = apv
        self._package = package
        self._category = category

    @property
    def apv(self):
        """Get Alcohol Per Volume of Drink"""
        return self._apv

    @apv.setter
    def apv(self, apv):
        """Set Alcohol Per Volume of Drink"""
        self._apv = apv

    @property
    def package(self):
        """Get Package type of Drink"""
        return self._package

    @package.setter
    def package(self, package):
        """Set Package type of drink"""
        self._package = package

    @property
    def category(self):
        """Get Category of drink"""
        return self._category

    @category.setter
    def category(self, category):
        """Set category of drink"""
        self._category = category

    def dumps(self):
        """Dump JSON data of object"""
        return json.dumps(self, ensure_ascii=True, cls=JSONEncoder, indent=4)

    def __str__(self):
        s = "Name: %s\nCost: %s\nAlcohol: %g%%\nPackaging: %s\nCategory: %s\nDescription: %s\n" % \
               (self.name, '${:,.2f}'.format(float(self.cost)/100.), self.apv / 10, self.package, self.category,
                self.desc)
        for param in self.unique_params:
            s += "%s: %s\n" % (param, self.unique_params[param])

        s += "\n\n************JSON**********\n%s" % self.dumps()

        return s
