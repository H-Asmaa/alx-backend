#!/usr/bin/env python3
"""
0x01. Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least recently used Cache (FIFO)."""

    def __init__(self):
        """The init of the class."""
        super().__init__()
        self.frequencyList = []

    def put(self, key, item):
        """A method that adds an item to the cache"""
        if item and key:
            if key in self.cache_data:
                self.frequencyList.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                leastUsedItem = self.frequencyList.pop(0)
                del self.cache_data[leastUsedItem]
                print("DISCARD: {}".format(leastUsedItem))
            self.cache_data[key] = item
            self.frequencyList.append(key)

    def get(self, key):
        """A method that gets data from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequencyList.remove(key)
        self.frequencyList.append(key)
        return self.cache_data[key]
