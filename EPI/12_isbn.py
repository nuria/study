#!usr/local/bin

from collections import OrderedDict
import unittest

# OrderedDict is a dic that remembers the order
# in which entries were added
# deleting an entry and re-inserting it will move it to the end
# the popItem(last=True) function returns items in LIFO order
# and FIFO if last is false

# the eveytime we lookup an entry we can move it to end and return oldest
# to evict from cache with popItem(last=False)
# move_to_end

class LruCache:

    def __init__(self, capacity=10):
        # like Map<int, int>
        self.cache = OrderedDict()
        self.capacity = capacity

    # if present, freshness is updated
    def _lookup(self, _id):
        if  self.cache.get(_id) is not None:
            # update frequency of key being acessed
            # by deleting it and inserting it again
            self.cache.pop(_id)
            self.cache[_id] = item
            return self.cache.get(_id)
        return -1

    def insert(self, _id, item):
        # if entry is in cache just update its freshness
        if _lookup(_id) != -1:
            return
        # is cache at capacity?
        # if so  we have to drop
        inserted = len(list(self.cache.items()))
        if inserted  == capacity:
            # we need to delete before inserting
            # delete the item that was acessed the longest time ago
            self.cache.popItem(last= False)
        self.cache[_id] = item

    def erase(self, _id, item):
        if self.cache.get(_id) is not None:
            self.cache.popItem(_id)
            return True
        else:
            return False

class testing(unittest.TestCase):
    def test_happy_case(self):
        lru = LruCache()
        lookup = lru._lookup(4)
        self.assertEqual(lookup, -1)


if __name__=="__main__":

    lru = LruCache()
    unittest.main().result


