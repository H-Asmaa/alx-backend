#!/usr/bin/env python3
"""
0x01. Caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching implementation."""

    def put(self, key, item):
        """A method that adds an item to the cache."""
        if item is None or key is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """A method that gets an item from the cache"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
