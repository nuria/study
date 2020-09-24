#!usr/local/bin

import sys
import unittest
import ast
# get an array that represents a non negative decimal integer
# and increment in one so [1,2,9] becomes->[1,3,0]

def add_one(n):
    # we can transform to int add one, and transform to list again
    n_int = int("".join(map(str,n)))
    n_int = n_int +1

    print n_int
    return map(int, list(str(n_int)))

def add_one_carry(n):
    # ok now let's add like to teh last number
    # if last number is '9' we need to carry
    if n[-1] != 9:
        n[-1] = n[-1] + 1
        return n
    # last number is 9
    return add_one_carry(n[0:len(n)-1]) + [0]


class testing(unittest.TestCase):

    def test_happy_case(self):
        l_plus_one = add_one_carry([1,2,8])
        self.assertEqual([1,2,9], l_plus_one)

    def test_carry_case(self):
        l_plus_one = add_one_carry([1,2,9])
        self.assertEqual([1,3,0], l_plus_one)

if __name__== "__main__":
    unittest.main().result

