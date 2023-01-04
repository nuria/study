#!/usr/local/bin

import sys
import unittest
import heapq 

def _sort(I):
   # hardcoding to thre arrays but input can be an array of arrays
    h = []
    MAX_LEN = 0
    i = 0 # index we are iterating on input arrays
    for a in I:
        MAX_LEN= max(len(a), MAX_LEN)
        # heap has len(I) elements
        heapq.heappush(h, a[i])

    result = []
    
    result.append(heapq.heappop(h))

    while i < MAX_LEN:
        # add smallest element
        i = i + 1
        for a in I:
            if i < len(a):
                if a[i] < h[0]:
                    result.append(a[i])
                else:
                    heapq.heappush(h, a[i])
                    # this keeps heap height to O(log(Len(I))) where i is the array of arrays
                    result.append(heapq.heappop(h))
        i = i + 1

    while len(h) > 0:
        result.append(heapq.heappop(h))

    return result



class TestSuite(unittest.TestCase):

    def test_happy_case(self):
        A1 = [3,5,7]
        A2 = [0,6]
        A3 = [0,6, 28]
        result = _sort([A1,A2,A3])
        self.assertTrue([0,0,3,5,6,6,7,28])    


    


if __name__=="__main__":
    unittest.main().result
