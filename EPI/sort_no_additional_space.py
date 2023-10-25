#!/usr/local/bin
import unittest


""" 
     A = [1,2]
     B = [3,4,5,x,y]
     
     size of A is always equal to x elements on B
     you have to return ; [1,2,3,4,5] w/o using additional space
     both A and B are sorted, quick sort does not use that fact 

    [1,2]
    [3,4,5,x,y]
    p1 = 0

    [3,2]
    [1,4,5,x, y]
    p1 = 1

    [3,4]
    [1,2,5,x,y]
    
    [5,4]
    [1,2,3,x,y]
    
    [1,2,3,4,5]

    treating A array as a circular buffer


"""

def qs(A):
    # this is nlogn
    pass

def circular(A, B):
    # this is o(n)
    
    # pointer to A , needs to be a circular buffer
    p1 = 0
    # pointer to B
    p2 =0

    # we use zero to exit 
    while p2 < len(B) and B[p2] !=-0:
        p1 = p1 % len(A)

        
        # use A array as a temporary repository of elements out of place
        if B[p2] > A[p1]:
            # swap 
            B[p2], A[p1] = A[p1], B[p2]
            # this is the smallest element
            p2 = p2 + 1
            p1 = p1 + 1
        else:
            # element on B array is in its place
            p2 = p2 + 1

    # now dump whatever if left in A to B
    # but we need to do it in order

    while p2 <len(B):
        p1 = p1 % len(A)
        B[p2] = A[p1]
        p2 = p2 + 1
        p1 = p1 + 1
            

    return B




class TestCase(unittest.TestCase):
    def test_happy_case(self):
        A = [1,2]
        B = [4,5,6, 0, 0]
        self.assertEqual(circular(A,B), [1,2,4,5,6])
        A = [4,5,6]
        B = [1,2,3,0,0,0]
        self.assertEqual(circular(A,B), [1,2,3,4,5,6])



if __name__=="__main__":
    unittest.main().result
