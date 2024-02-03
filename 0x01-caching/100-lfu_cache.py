#!/usr/bin/env python3
"""
0x01. Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used Cache (LFU)."""

    def __init__(self):
        """The init of the class."""
        super().__init__()
        self.frequencyCounter = {key: 0 for key in self.cache_data.keys()}

    def put(self, key, item):
        """A method that adds an item to the cache"""
        if item and key:
            if key in self.cache_data:
                del self.frequencyCounter[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """In case where there are two keys with the same value
                the function will get the first one."""
                Least_FR_UsedItem = min(
                    self.frequencyCounter, key=self.frequencyCounter.get
                )
                del self.frequencyCounter[Least_FR_UsedItem]
                del self.cache_data[Least_FR_UsedItem]
                print("DISCARD: {}".format(Least_FR_UsedItem))
            self.cache_data[key] = item
            self.frequencyCounter[key] = 0

    def get(self, key):
        """A method that gets data from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        UseCount = self.frequencyCounter[key] + 1
        del self.frequencyCounter[key]
        self.frequencyCounter[key] = UseCount
        return self.cache_data[key]
