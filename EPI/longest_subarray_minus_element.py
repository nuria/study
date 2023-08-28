#!/usr/local/bin
"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.
"""

import unittest


def get_max_ones(A):
   
    print ("input: {0}".format(A))
    # we can have two arrys right and left
    # left is the number of 1s that finish at index i
    # right is the number of ones that start at index i
    # (both not counting i)
    # the max(sum of both) is the longest 1 subarray 
    # o(n) time and o(n) space

    right = [0] *len(A)
    left = [0] *len(A)

    len_left = 0
    len_right = 0

    for i in range(0, len(A)):
        

        if A[i] == 0:
            len_left = 0
        else:
            len_left +=1
            left[i] = len_left

    A.reverse()
    
    print(A)

    len_left = 0
    # same problem reverse gives us the  sequence that starts at i
    for i in range(0, len(A)):
        
        
        print (right)
        
        if A[i] == 0:
            len_left = 0
        else:
            len_left +=1
            right[i] = len_left 

    right.reverse()

    print("Left: {0}".format(left))
    print ("Right: {0}".format(right))

    #remove the first 0 , does it have to be the max?

    _max = 0
    for j in range(0, len(left)):
        # this is the 1st we find
        seq = 0
        if j > 0:
            seq = left[j-1]
        if j < len(left) -1:
            seq = seq + right[j+1]
        if seq > _max:
            _max = seq

    return _max

class TestSuite(unittest.TestCase):

    def test_happy_case(self):
        A = [1,1,0,1]
        self.assertEqual(3,get_max_ones(A))
        # output should be  3
        A =[0,1,1,1,0,1,1,0,1]
        self.assertEqual(5,get_max_ones(A))
        # output should be 5
        A = [1,1,1]
        # output should be two
        self.assertEqual(2,get_max_ones(A))
        
        
    


if __name__=="__main__":
    unittest.main().result
