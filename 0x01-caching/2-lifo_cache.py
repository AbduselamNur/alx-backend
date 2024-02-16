#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.order.pop()
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
                    self.order.append(key)
                else:
                    self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
