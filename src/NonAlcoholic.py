#!/usr/bin/python
from .Drink import Drink


class NonAlcoholic (Drink):
    """Inherited class of Drink containing all Non-alcoholic beverages
        All Non-Alcoholic Beverages also have carbonationState, sugar content, package, and caffeine content"""

    def __init__(self, did, name, cost, desc, is_carbonated, sugar_content, package, caffeine_content):
        super().__init__(did, name, cost, desc)
        self._is_carbonated = is_carbonated
        self._sugar_content = sugar_content
        self._package = package
        self._caffeine_content = caffeine_content

    @property
    def is_carbonated(self):
        """Get property of whether or not drink is carbonated"""
        return self._is_carbonated

    @is_carbonated.setter
    def is_carbonated(self, is_carbonated):
        """Set property of whether or not drink is carbonated"""
        self._is_carbonated = is_carbonated

    @property
    def sugar_content(self):
        """Get sugar content of drink"""
        return self._sugar_content

    @sugar_content.setter
    def sugar_content(self, sugar_content):
        """Set sugar content of drink"""
        self._sugar_content = sugar_content

    @property
    def package(self):
        """Get Package content of drink"""
        return self._package

    @package.setter
    def package(self, package):
        """Set Package content of drink"""
        self._package = package

    @property
    def caffeine_content(self):
        """Get Caffeine content of drink"""
        return self._caffeine_content

    @caffeine_content.setter
    def caffeine_content(self, caffeine_content):
        """Set Caffeine content of drink"""
        self._caffeine_content = caffeine_content

    def __str__(self):
        str_carbonated = 'Yes' if self.is_carbonated else 'No'
        return "Name: %s\nCost: %g$\nDescription: %s\nCarbonated: %s\nSugar Content: %s\nPackage: %s\n" \
               "Caffeine Content: %s" % (self.name, self.cost / 100, self.desc, str_carbonated, self.sugar_content,
                                         self.package, self.caffeine_content)
