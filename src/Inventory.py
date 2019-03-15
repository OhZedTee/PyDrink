#!/usr/bin/python

from .DrinkStorage import DrinkStorage
from .Alcoholic import Alcoholic
from .NonAlcoholic import NonAlcoholic
import urllib.request
import json
import re
import yaml


class Inventory(DrinkStorage):
    """Implementation of Abstract management class for all Drinks.
       This class manages all drinks a user has available (not necessarily planning to use for cocktails"""

    def __init__(self):
        super().__init__()
        self._host = "localhost"
        self._port = "3000"
        self._page = 1
        self._num_pages = 0
        self._final_page = False
        self._is_search = False
        self._search_params = None
        self.config()
        self.get_products()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

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
    def is_search(self, value):
        self._is_search = value

    @property
    def search_params(self):
        return self._search_params

    @search_params.setter
    def search_params(self, value):
        self._search_params = value

    # Pre: Config file must exist
    # Post: API host and port for LCBO API loaded from config file
    def config(self):
        with open("data/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.host = cfg['API']['host']
        self.port = cfg['API']['port']

    # Pre: api_return must be a valid JSON dictionary response from LCBO API
    # Post: Parses data from LCBO API and add drinks to dictionary of drinks
    def parse(self, api_return):
        """Method to parse JSON data from API into dictionary"""
        self.final_page = api_return['pager']['is_final_page']
        self.num_pages =  api_return['pager']['total_pages']
        results = api_return['result']
        for item in results:
            category = []
            for attribute in item:
                if "category" in attribute.lower():
                    category.append(item[attribute])

            if "vermouth" in str(item['name']).lower():
                if "dry" in str(item['name']).lower():
                    category.append("Dry")
                elif "sweet" in item['name'].lower():
                    category.append("Sweet")

            d = Alcoholic(item['id'], item['name'], item['regular_price_in_cents'], item['tasting_note'],
                          item['alcohol_content'] / 10, item['package'], category)

            for param in item:
                if item[param] not in category and param != 'id' and param != 'name' \
                        and param != 'regular_price_in_cents' and param != 'tasting_note' \
                        and param != 'alcohol_content' and param != 'package' and param != 'image_thumb_url' \
                        and param != 'updated_at' and param != 'image_url' and item[param] is not False\
                        and item[param] is not None:
                        # Convert snake_case to readable Snake Case

                        def print_case(match):
                            return match.group(1) + " " + match.group(2)

                        # replace snake case with space separated Pascal Case
                        key =  re.sub(r"(.*?)_([a-zA-Z])", print_case, param, 0)
                        d.add_unique_param(key.title(), item[param])

            # duplicates found in API, if duplicates fixed in API, this can be removed
            if self.find_drink('name', d.name) is None:
                self.add_drink(d)

    # Pre: if category is provided, must be valid string
    # Post: Parses drink data returned from API in JSON format and stores in dictionary of drinks
    def get_products(self, category=None):
        self.clear_drinks()
        if category is not None:
            params = urllib.parse.urlencode({'page': self.page, 'q': category})
        else:
            params = urllib.parse.urlencode({'page': self.page})
        url = 'http://%s:%s/products?%s' % (self.host, self.port, params)
        req = urllib.request.Request(url)
        req.method = 'GET'
        try:
            with urllib.request.urlopen(req) as jsonobj:
                contents = json.loads(jsonobj.read().decode('utf-8'))
                self.parse(contents)
        except TimeoutError:
            print("LCBO API NOT CONNECTED")
        except urllib.error.URLError:
            print("LCBO API NOT CONNECTED")
