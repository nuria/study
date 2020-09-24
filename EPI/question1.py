#!usr/local/bin/python

# Fastest way to count number of bits in a 32-bit or 64-bit integer.

import unittest
def count_bits(n):
    # how can you count bits, can you and with 1
    i = 0
    tally = 0
    print n
    while (n >>i > 0):
        if (n >>i  & 1 == 1):
            tally += 1
        i += 1

    return tally

class Testing(unittest.TestCase):
    def test_happy_case(self):
        self.assertEqual(count_bits(16777216), 1)
        self.assertEqual(count_bits(15),4)

if __name__=="__main__":

    # 1 00000...000 (2 ^24)
    unittest.main().result

