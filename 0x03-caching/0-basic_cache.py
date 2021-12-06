#!/usr/bin/env python3
""" Module for Basic Dictionary """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class that set and get itmes from a dict """

    def put(self, key, item):
        """ function that set an item to the dict """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ function that get the item from the dict """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
