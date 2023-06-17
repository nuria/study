#!/usr/local/bin

# implement a fifo queue with enque deque and max operations
# we can use a heap rather than a sorted list as an additional structure
# 
import unittest
from collections import deque 

class QMax():
    def __init__(self):
        # what is the data structure we are going to use?
        # two fifo queues
        # keeps track of maximuns
        self.D = deque([]) 
        self.Q = deque([])

    def max_item(self):
        if len(self.D) > 0:
            return self.D[0]
        else:
            return None
    
    # every addition is a O(1)
    # but lookups in the middle of a deque are o(n), careful
    def add(self, item):
        if len(self.Q) < 1:
            self.Q.append(item)
            self.D.append(item)
        else:
            self.Q.append(item)
            if item > self.D[-1]:
                # pop the max that is super seeded by this new entry
                self.D.pop()
            self.D.append(item)

    # FIFO queue , removes element
    # and updates max queue if needed
    def pop(self):
        # pops FIFO entered
        item = self.Q.popleft()
        if item == self.D[0]:
            self.D.popleft()
        return item

    def __repr__(self):
        return "Q: {0}, D:{1}".format(self.Q, self.D)



class TestSuite(unittest.TestCase):
    def test_happy_case(self):
        q = QMax()
        for i in [3,1,3,2,0]:
            q.add(i)
        print(q)
        self.assertEqual(q.max_item(), 3)
        q.add(1)
        print(q)
        q.pop()
        print(q)
        q.pop()
        print(q)
        q.add(2)
        print(q)
if __name__=="__main__":
    unittest.main().result
