#!usr/local/bin/python
# design a stack that includes a max operation in addition to push and pop
# push -> append
# pop _ > pushes the last element

import unittest

class iStack():
    def __init__(self, l):
        # l is really the stack
        self.l = l
        # we could keep track with a heap
        # but how about a hashmap to cache
        # what was the maximun BEFORE we inserted
        # the item in question
        self._max = None
        self.m = {}

    def push(self, item):
        self.l.append(item)
        # cache what was the maximun before we entered this item
        self.m[item] = self._max
        if item > self._max or self._max is None:
           self._max  = item

    def pop(self):
        item = self.l.pop()
        if item == self._max:
            # we are popping the maximun, update
            self._max = self.m[self._max]
            del self.m[self._max]
        return item


    """
    Returns the max of the stack, has to be more than a pointer cause otherwise
    if we pop the max we do not know which is the max
    """
    def max(self):
        return self._max

    def __str__(self):
        return str(self.l)


class testing(unittest.TestCase):

    def setUp(self):
        self.s = iStack(list())
        self.s.push(5)
        self.s.push(4)
        self.s.push(1)
        self.s.push(0)

    def test_happy_case(self):
        print self.s
        self.assertEqual(self.s.pop(), 0)
        self.assertEqual(self.s.max(), 5)


if __name__=="__main__":
    unittest.main().result

