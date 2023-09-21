#!/usr/local/bin

import sys
import unittest

# find  element or next largest to a given one in a sorted array, binary search

def binary_s(A,t):
    
    
    A.sort()

    L = 0

    U = len(A)-1

    while U > L:
        m = int(L + (U-L)/2)

        if A[m] > t:
            # we pass the target, go back
            U = m -1
        elif A[m]< t:
            # go forward
            L = m +1
        else:
            return A[m]

    return A[m]


class TestCase(unittest.TestCase):
    
    def test_happy(self):
        A = [7, 43,110,114]
        t = 112
        self.assertTrue(binary_s(A,t),114 )

        A= [1,2,3,4,5,6,7,9]
        t = 8
        self.assertTrue(binary_s(A,t),9)



if __name__=="__main__":
    unittest.main().result
