#!/usr/bin/python


class Drink:
    """Common base class for all beverages
        All Drinks have a drink ID (did), a name, cost, and description"""

    def __init__(self, did, name, cost, desc):
        self._id = did
        self._name = name
        self._cost = cost
        self._desc = desc
        self._selected = False

    @property
    def id(self):
        """Unique Id of drink"""
        return self._id

    @property
    def name(self):
        """Get Name of drink"""
        return self._name

    @name.setter
    def name(self, name):
        """Set Name of drink"""
        self._name = name

    @property
    def cost(self):
        """Get Cost of drink"""
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Set Cost of drink"""
        self._cost = cost

    @property
    def desc(self):
        """Get Description of drink"""
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Set Description of drink"""
        self._desc = desc

    @property
    def selected(self):
        """Get Selected property of drink"""
        return self._selected

    @selected.setter
    def selected(self, value):
        """Set Selected property of drink"""
        self._selected = value

    def __str__(self):
        return "Name: %s\nCost: %g$\nDescription: %s\n" % (self.name, self.cost, self.desc)
