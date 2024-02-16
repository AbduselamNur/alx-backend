#!/usr/bin/env python3
""" LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            value = key not in self.cache_data
            if len(self.cache_data) >= self.MAX_ITEMS and value:
                discard = self.cache.pop(0)
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
            self.cache_data[key] = item
            if key in self.cache:
                self.cache.remove(key)
            self.cache.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.cache.remove(key)
            self.cache.append(key)
            return self.cache_data[key]
        return None
