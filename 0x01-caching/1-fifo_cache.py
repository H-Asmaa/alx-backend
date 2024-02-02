#!/usr/bin/env python3
"""
0x01. Caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First In, First Out Cache (FIFO)."""

    def __init__(self):
        """The init of the class."""
        super().__init__()

    def put(self, key, item):
        """A method that adds an item to the cache"""
        if item is None or key is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey = next(iter(self.cache_data))
            del self.cache_data[firstKey]
            self.cache_data[key] = item
            print("DISCARD: {}".format(str(firstKey)))
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """A method that gets data from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
