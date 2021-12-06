#!/usr/bin/env python3
""" Module for FIFO Dictionary """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO class """

    def __init__(self):
        """ overload init """
        super().__init__()
        self.__datakeys = []

    def put(self, key, item):
        """ function that put items in dict """

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.__datakeys:
            discard = self.__datakeys.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

        if key and item:
            self.__datakeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ function that get the item from the dict """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
