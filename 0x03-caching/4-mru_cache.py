#!/usr/bin/env python3
""" Module for MRU Dictionary """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Class """

    def __init__(self):
        """ overload init """
        super().__init__()
        self.__datakeys = []

    def put(self, key, item):
        """ function that put items in dict """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.__datakeys:
            discard = self.__datakeys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

        if key and item:
            if key not in self.cache_data:
                self.__datakeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ function that get the item from the dict """
        if not key or key not in self.cache_data:
            return None
        else:
            self.__datakeys.remove(key)
            self.__datakeys.append(key)
            return self.cache_data[key]
