# The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
# get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
# set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
# In the constructor of the class the size of the cache should be intitialized.

# Input:
# The first line of input contain an integer T denoting the number of test cases. Then T test case follow. Each test case contains 3 lines. The first line of input contains an integer N denoting the capacity of the cache and then in the next line is an integer Q denoting the number of queries Then Q queries follow. A Query can be of two types
# 1. SET x y : sets the value of the key x with value y
# 2. GET x : gets the key of x if present else returns -1.

# Output:
# For each test case, in a new line, output will be space separated values of the query.

class LRUCacheValue:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
    
    def updatePos(self, pos):
        self.pos = pos

    def updateValue(self, val):
        self.val = val

class LRUListValue:
    def __init__(self, key):
        self.key = key

class LRUCache:
        
    def __init__(self,cap):
        # cap:  capacity of cache
        #Intialize all variable
        #code here
        self.cache = {}
        self.tracker = []
        self.maxSize = cap
        self.size = 0
    
    def updateTracker(self, key):
        posInList = self.cache[key].pos
        self.tracker.remove(posInList)
        self.tracker.append(posInList)
        # self.cache[key].updatePos(temp)

    def addItemToCache(self, key, value):
        track = LRUListValue(key)
        self.tracker.append(track)
        self.cache[key] = LRUCacheValue(value, track)

    #This method works in O(1)
    def get(self, key):
        #code here
        if key in self.cache:
            self.updateTracker(key)
            return self.cache[key].val
        else:
            return -1
        
        
    #This method works in O(1)   
    def set(self, key, value):
        #code here
        if key in self.cache:
            #Update position in list
            self.updateTracker(key)
            self.cache[key].updateValue(value)
        else:
            #if cache size is less than capacity
            if self.size < self.maxSize:
                self.addItemToCache(key, value)
                self.size += 1
            #if cache size is equal to capacity
            elif self.size == self.maxSize:
                itemToBeRemoved = self.tracker[0]
                del(self.cache[itemToBeRemoved.key])
                del(self.tracker[0])
                self.addItemToCache(key, value)


lru = LRUCache(2)
lru.set(1,2)
lru.set(2,3)
lru.set(1,5)
lru.set(4,5)
lru.set(6,7)
print(lru.get(4))
print(lru.get(1))

# lru = LRUCache(4)
# lru.set('a',2)
# lru.set('b',3)
# lru.set('c',5)
# lru.set('d',5)
# print(lru.get('b'))
# print(lru.get('c'))
# print(lru.get('a'))
# print(lru.get('c'))

