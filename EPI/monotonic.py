#!/usr/local/bin

# monotonic increasing stack from a list
# https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/

import sys
import unittest

def monotonic_i(A):
    # creates a monotonic starting stack from a list
    m = []
    m.append(A[0])
    
    for a in A[1:]:
        #admits equal elements
        while( len(m) > 0 and a < m[-1]):
            m.pop()

        m.append(a)

    return m



def monotonic_d(A):
    # creates a monotonic starting stack from a list
    m = []
    m.append(A[0])
    
    for a in A[1:]:
        #admits equal elements
        while( len(m) > 0 and a > m[-1]):
            m.pop()

        m.append(a)

    return m


def check_next_greatest(T):
    pass



    
class TestCase(unittest.TestCase):
    def test_happy_case(self):
        mi = monotonic_i([1,4,5,3,12,10])

        # this should leave us [1,3,10]
        self.assertEqual(mi, [1,3,10])

        md = monotonic_d([15, 17, 12, 13, 14, 10])
        self.assertEqual(md,[17,14,10])

    def test_next_greatest(self):
        t = [73,74,75,71,69,72,76,73]
        pass

if __name__=="__main__":
    unittest.main().result
