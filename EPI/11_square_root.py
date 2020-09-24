#!usr/local/bin
# find suare root of a number using binary search
import sys
import random
import unittest

def binary_search(target, start,end):
    print "{0} {1}".format(start, end)
    # case zero
    if end - start == 1:
        # value is one of the two of the interval
        if target - (end * end) >= 0:
            return end
        else:
            return start


    middle = int((end-start)/2)

    middle = start + middle

    # try larger interval first
    if (middle+1) * (middle+1) <= target and target <= end* end:
        return binary_search(target, middle + 1 , end)
    else:
        # since we are looking for the smaller integer,
        # default is smaller interval
        return binary_search(target, start, middle)

def find_sqrt(n):
    # first let's try to find the closest integer
    # find square root of a number using binary search
    # the square root of a number needs to be between (1 and n/2)
    return binary_search(n, 1, int(n/2))


class testing(unittest.TestCase):
    def test_happy_case(self):
        self.assertEqual( find_sqrt(16), 4)
        print find_sqrt(300)
        self.assertEqual(find_sqrt(300), 17)

if __name__=="__main__":

    unittest.main().result

