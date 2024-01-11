#!/usr/local/bin
import unittest

def flip(arr,k):
    r = int(k/2)
    k = k - 1
    # flips 1st k positions on array
    for i in range(0,r):
        tmp = arr[i]
        arr[i] = arr[k-i]
        arr[k-i] = tmp

    return arr


class TestCase (unittest.TestCase):
    def test_happy(self):
        a = [1,3,4,5,100]
        self.assertEqual( flip([1, 2, 3, 4, 5],2), [2,1,3,4,5] )
        self.assertEqual( flip([1, 2, 3, 4, 5],4), [4,3,2,1,5] )

if __name__=="__main__":
    unittest.main().result
