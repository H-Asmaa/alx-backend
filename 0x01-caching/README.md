# 0x01-caching
### Table of content
- [Introduction to caching](#introduction-to-caching)
- [What FIFO means](#what-fifo-means)
- [What LIFO means](#what-lifo-means)
- [What LRU means](#what-lru-means)
- [What MRU means](#what-mru-means)
- [What LFU means](#what-lfu-means)
- [What the purpose of a caching system](#what-is-the-purpose-of-a-caching-system)
- [What limits a caching system have](#what-limits-a-caching-system-have)

## Introduction to caching
You know when you wear a peice of clothing and you keep it in an easily accessible place so that you can get it fast. There might be different reasons for that, the peice of clothes might be one of your favorites, or it might be because you wear it more often...

same for caching, the caching is a technique in computing to store and manage data that can be reused. It allows faster access to frequently used information by storing it in memory.

This technique can be implemented in hardware as well as in software... There are different algorithms that can be used to acheive such thing, which are exactly what we are going to extend in in this file.

## What FIFO means
First in First Out. It is a Queue like structure. The data which comes first will be removed first.
```python
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
```
The above is a class where we tested how FIFO works in caching. The class has two methods put that adds an item to the cache and the method get that gets an item from a cache.

## What LIFO means
Last in First Out. It is a Stack like structure. The last data most recently added is the first to be removed.
```python
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
```

## What LRU means
Least Recently Used. The data least recently used will be removed. It is often done using timestamp or a counter.
```python
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
```

## What MRU means
Most Recently Used. The data most recently used will be removed.
```python
class MRUCache(BaseCaching):
    """Most Recently Used Cache (FIFO)."""

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
                MostUsedItem = self.frequencyList.pop(len(
                    self.frequencyList
                    ) - 1)
                del self.cache_data[MostUsedItem]
                print("DISCARD: {}".format(MostUsedItem))
            self.cache_data[key] = item
            self.frequencyList.append(key)

    def get(self, key):
        """A method that gets data from cache by key"""
        if key is None or key not in self.cache_data:
            return None
        self.frequencyList.remove(key)
        self.frequencyList.append(key)
        return self.cache_data[key]
```


## What LFU means
Least Freaquently Used. The data least freaquently used will be removed first.
```python
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
```

## What is the purpose of a caching system
The purpose of the caching system is to make data retrieval faster and more accessible. It also helps minimize the latency related to data fetching since it keeps a copy of used data. This conserves resources as well ...
## What limits a caching system have
One of the limitations that can come to mind is the update of data. Keeping data in the cache is great be we have to make sure that data is being updated when necessary.
