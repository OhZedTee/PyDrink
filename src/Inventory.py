#!/usr/bin/python

from .Manager import Manager
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
import urllib.request
import json


class Inventory(Manager):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()
        self._page = 1
        self._num_pages = 0
        self._final_page = False
        self._is_search = False
        self._search_params = None
        self.get_products()

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, page):
        if page > 0:
            self._page = page

    @property
    def num_pages(self):
        return self._num_pages

    @num_pages.setter
    def num_pages(self, num_pages):
        if num_pages > 0:
            self._num_pages = num_pages

    @property
    def final_page(self):
        return self._final_page

    @final_page.setter
    def final_page(self, value):
        self._final_page = value

    @property
    def is_search(self):
        return self._is_search

    @is_search.setter
    def final_page(self, value):
        self._is_search = value

    @property
    def search_params(self):
        return self._search_params

    @search_params.setter
    def search_params(self, value):
        self._search_params = value

    def parse(self, fp):
        """Method to parse JSON data from API into dictionary"""
        self.final_page = fp['pager']['is_final_page']
        self.num_pages =  fp['pager']['total_pages']
        results = fp['result']
        for item in results:
            d = Alcoholic(item['id'], item['name'], item['regular_price_in_cents'], item['tasting_note'],
                          item['alcohol_content'] / 10, item['package'], item['primary_category'])

            # duplicates found in API, if duplicates fixed in API, this can be removed
            if self.find_drink('name', d.name) is None:
                self.add_drink(d)

    def get_products(self, category=None):
        self.clear_drinks()
        if category is not None:
            params = urllib.parse.urlencode({'page': self.page, 'q': category})
        else:
            params = urllib.parse.urlencode({'page': self.page})
        url = 'http://localhost:3000/products?%s' % params
        req = urllib.request.Request(url)
        req.method = 'GET'
        with urllib.request.urlopen(req) as jsonobj:
            contents = json.loads(jsonobj.read().decode('utf-8'))
            self.parse(contents)
            #item = str(contents)
            #print(item)

