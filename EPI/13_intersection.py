#!usr/local/bin
# find the intersection of sorted arrays

import unittest
import collections

def intersection_better(a,b):
    result = set()

    # work with two indexes moving on both arrays
    a_iter = iter(a)
    b_iter= iter(b)

    next_a = next(a_iter)
    next_b = next(b_iter)
    o(m +n)
    while True:
        try:
            if next_a < next_b:
                # there is no commonality here
                # advance a
                next_a = next(a_iter)
            elif next_a > next_b:
                #advance b
                next_b = next(b_iter)
            else:
                result.add(next_a)
                next_a = next(a_iter)
                next_b = next(b_iter)
        except StopIteration:
            break

    return result

def intersection(a,b):

    # we can do similarly
    # to the smerge step on merge sort
    result = set()
    # we can put array a on a hashmap and do a lookup
    # O(n) space plus o(n) time plus space of result array
    a_map = collections.Counter(a)

    for item in b:
        if a_map.get(item):
            # no effect if item is there o(1)
            result.add(item)

    return result

class testing(unittest.TestCase):
    def test_happy_case(self):
        a = [2,3,3,5,5,6,7,7,8,12]
        b = [5,5,6,8,8,9,10,10]
        self.assertEqual( sorted(intersection_better(a,b)), [5,6,8])

if __name__=="__main__":

    unittest.main().result
