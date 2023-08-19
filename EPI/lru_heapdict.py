#/usr/local/bin

import unittest
import heapdict
from datetime import datetime
import pprint

# LRU cache, keeps capacity items on 
# when we reach capacity +1 the LRU is dropped

class Cache():

    def __init__(self, capacity=100):
        self.capacity = capacity
        
        # items are available for fast lookup as key/value pairs
        self.items = {}
        
        # we also need to keep track of access
        # can we use a heapdict?
        self.heap = heapdict.heapdict()

        # self.heap[obj1] = priority1
        # returns item with lowest priority
        # (obj, priority) = hd.popitem()

    def debug(self):
        for k in self.heap.keys():
            print("key: {0}. value:{1}".format(k, self.heap[k]))


    def put(self, key, value):
        # adds an item to the cache
        # if capacity is breached drops LRU
        
        if len(self.items.keys()) >= self.capacity:
            self.debug()
            # drop least recently used item
            (lru_key, priority) = self.heap.popitem()
            
            # delete from cache
            print ('deleting from cache. key:{0}'.format(lru_key))
            
            self.items.pop(lru_key)

        # now, add new key
        self.items[key] = value
        
        # using time for priority, earliest access, min number of seconds
        self.heap[key] = datetime.now().timestamp() 
        self.debug() 

    def get(self, key):
        if self.items.get(key) is not None:
            # update LRU marker
            
            self.heap[key] = datetime.now().timestamp() 
            return self.items[key]
        else:
            return None


class TestSuite(unittest.TestCase):

    def test_happy_case(self):
        cache = Cache(1)
        cache.put('a', 'A')
        self.assertTrue(cache.get('a') == 'A')
    
    def test_eviction(self):
        cache = Cache(2)
        cache.put('a', 'A')
        cache.put('b', 'B')
        self.assertTrue(cache.get('b') == 'B')
        cache.put('c', 'C')
        self.assertTrue(cache.get('a') ==  None)
        self.assertTrue(cache.get('c') == 'C')


if __name__=="__main__":
    unittest.main().result
