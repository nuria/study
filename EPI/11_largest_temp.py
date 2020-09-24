#!usr/local/bin
import unittest

import random

def k_largest(a,k):
    if len(a) == 0:
        return a
    p = random.choice(a)

    for i in a:
        large = []
        small = []
        if i ==p :
            next
        elif i > p:
            large.append(p)
        else:
            small.append(p)

        # now look at cardinal

        if len(large) >= k:
            return k_largest(large,k)
        else:
            return k_largest(large,k) + [p]+ k_largest(small,k)


class testing(unittest.TestCase):
    def test_happy_case(self):
        a = [3, 2,1,5,4]
        ak = k_largest(a,3)
        print ak
        self.assertEqual(ak[2], 3)


if __name__=="__main__":
    unittest.main().result

