#!/usr/local/bin

import heapdict as h
# hd[obj1] = priority1
# hd[obj2] = priority2


class simplecache():

    def __init__(self, size=10):
        self.cache = {}
        self.heap = h.heapdict()
        self.size = size

    # updates the value if present 
    # put will enter into heap as well
    # or update the count of usage of item
    # h[item] = update_count_of_usage
    def put(self,_id, value):
        _id = str(_id)
        if self.cache.get(_id) is None:
            # see if we are at capacity
            if len(self.cache.keys()) == self.size:
                self.expire_lfu()
            self.cache[_id] = None
            self.heap[_id] = 0

        self.cache[_id] = value
        self.heap[_id]+= 1

    def expire_lfu(self):
        # looks at heapdict top
        # removes top element from heap
        (_id, use) = self.heap.popitem()
        
        # removes top element from dic
        del self.cache[_id]

    def get(self,_id):
        _id = str(_id)
        if self.cache.get(_id) is None:
                return None
        else:
            self.heap[_id]+= 1
            return self.cache[_id]

    def __repr__(self):
        txt = ''
        keys = self.cache.keys()

        for k in keys:
            txt += " key:" +k+ " , value: " + self.cache[k]+", total access "+ str(self.heap[k])+"\n"

        return txt



cache = simplecache(2)

# should return None
print cache.get("7")

cache.put("7", "the best number")
print cache
cache.put("5", "the easy number")
print cache

# should return value
print cache.get("7")

cache.put("77", "favorite number")
print cache

# should return updated value
print cache.get("7")

cache.put(6, "favorite number again")
print cache.get("7")

print cache

