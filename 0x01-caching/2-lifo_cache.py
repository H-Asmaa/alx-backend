#!/usr/bin/env python3
"""
0x01. Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In, First Out Cache (LIFO)."""

    lastItemKey = None

    def __init__(self):
        """The init of the class."""
        super().__init__()

    def put(self, key, item):
        """A method that adds an item to the cache"""
        if item and key:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lastItemKey = key
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.lastItemKey]
                print("DISCARD: {}".format(self.lastItemKey))
            self.cache_data[key] = item
            self.lastItemKey = key

    def get(self, key):
        """A method that gets data from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
