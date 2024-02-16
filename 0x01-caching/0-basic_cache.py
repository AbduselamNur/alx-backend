#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache defines:
      - overwrite functions 'put' and 'get' for implement
        LIFO caching system
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data
            the item value for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
