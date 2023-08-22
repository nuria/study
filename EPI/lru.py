#!usr/local/bin

import unittest

# string of length 10
# 9 digits plus a check character wich is teh sum of the 1st 9 chars mod 11 10 represented by X

# an insert updates its position in the cache
# lookup if present most recent position in the cache, otherwise -1
# erase, true if present false otherwise

# what re trhe data structures we need here?
# lookups require a hash but to maintain a structure ordered in lookups
# we need to have a linked list? each entry on teh hash has to have previous and next
# for us to be able to update things so it is a doubly linked list 
# root of list is last element in terms of LRU

class node():
    def __init__(self, value, previous=None, nxt=None):
        self.value = value
        self.previous = previous
        self.next = nxt

    def __rpr__(self):
        txt = ''
        if self.previous is not None:
                txt +=self.previous.value 

        txt+="<-" + self.value+"->"
        if self.next is not None:
            txt += self.next .value
    

class lru():

    def __init__(self, capacity =10):
        self.cache = {}
        self.root = None
        self.last =  None
        self.capacity = capacity 


    def insert(self, _id, value):
        current_node = None

        if self.cache.get(_id) is  None:
            current_node = node(value)
            if self.root is None:
                self.root = current_node

            self.cache[_id] = current_node

            if self.last is not None:
                self.last.next = current_node
            self.last = current_node
        else:
            self.refresh(_id)

        if len(self.cache.keys()) > self.capacity:
                # evict root
                self.root = self.root.next
                self.root.previous = None
    
    def refresh(_id):
        # update position on LRU
        current_node = self.cache.get(_id)
        previous_node = node.previous
        next_node = node.next 
           
        if previous_node is not None:
            previous_node.next = next_node
        if next_node is not None:
                next_node.previous = previous_node
        
        if self.last is not None:
            self.last.next = current_node
        
        current_node.next = None
        self.last = current_node

    def lookup(self, _id):
        if self.cache.get(_id) is None:
            return -1
        else:
            insert(value)
            return self.cache[_id]

    def delete(self, _id):
        if self.cache.get(_id) is None:
            return False
        else:
            current_node = self.cache[_id]
            del self.cache[_id]
            
            
            previous_node = current_node.previous
            
            next_node = current_node.next
            if previous_node is not None:
                previous_node.next = next_node
            if next_node is not None:
                next_node.previous = previous_node
            
            # questionable equlity
            if self.last == current_node:
                self.last = current_node.previous
            if self.root == current_node:
                self.root = current_node.next

            return True
    
    def debug(self):
        print self.root


class TestCase(unittest.TestCase):

    def test_happy_case(self):
        cache = lru(2)
        cache.insert(1, 'patata')
        cache.insert(2, 'potato')
        self.assertTrue(cache.delete(2))
        self.assertFalse(cache.delete(3))



if __name__ =="__main__":
    unittest.main().results
