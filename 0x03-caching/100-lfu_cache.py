#!/usr/bin/python3
""" Module for LFU Dictionary """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LfU Class """

    def __init__(self):
        """ overload init """
        super().__init__()
        self.__datakeys = []
        self.__count = {}

    def put(self, key, item):
        """ function that put items in dict """
        if not key or not item:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.__datakeys:
            self.discard()
        if key not in self.cache_data:
            self.__count[key] = 1
        else:
            self.__count[key] += 1
            self.__datakeys.remove(key)
        self.__datakeys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ function that get the item from the dict """
        if not key or key not in self.cache_data:
            return None
        self.__count[key] += 1
        self.__datakeys.remove(key)
        self.__datakeys.append(key)
        return self.cache_data[key]

    def discard(self):
        """
        discard item and print
        """
        m_time = min(self.__count.values())
        keys = [k for k, v in self.__count.items() if v == m_time]
        low = 0
        while self.__datakeys[low] not in keys:
            low += 1
        discard = self.__datakeys.pop(low)
        del self.cache_data[discard]
        del self.__count[discard]
        print('DISCARD: {}'.format(discard))
