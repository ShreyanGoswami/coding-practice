# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.


class CacheItem:
    def __init__(self, val):
        self.val = val
        self.hit = 0

    def increment(self) -> None:
        self.hit = self.hit + 1


class LRUCache:
    cache = {}

    def __init__(self, capacity: int):
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            cached_item = self.cache.get(key)
            self.decreaseAge()
            cached_item.increment()
            return cached_item.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            key_to_evict = self.findMin()
            del self.cache[key_to_evict]
        self.cache[key] = CacheItem(value)
        if self.cap > 0:
            self.cap = self.cap - 1

    def findMin(self) -> int:
        min_hits = 1000000
        to_evict = -1
        for key, cached_item in self.cache.items():
            if min_hits > cached_item.hit:
                min_hits = cached_item.hit
                to_evict = key
        return to_evict

    def decreaseAge(self):
        for cached_item in self.cache.values():
            cached_item.hit = cached_item.hit - 1

    def getCache(self):
        return self.cache


# Questions
# What will happen if the cache has a single item left and we add one value and add another? Should the last one be evicted?

# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3) # Evict 2
# print(cache.get(2))
# cache.put(4, 4)  # Evict 1
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))

cache = LRUCache(1)
cache.put(2, 1)
print(cache.get(2))
cache.put(3, 2)
print(cache.get(2))
print(cache.get(3))
