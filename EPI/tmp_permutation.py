#!usr/local/bin

import unittest


def next_perm(L):
    # identify the point at which there is an inversion
    inversion = None
    for i in range(0, len(L)-1):
        if L[i+1] > L[i]:
            inversion = i + 1

    if inversion is None:
        return L

    candidate = L[inversion:]

    # now identify the smallest entry on the list
    # and swap that with index inversion-1
    _min = 0
    for c in range(0, len(candidate)):
        if candidate[c] < candidate[_min]:
            _min = c

    # swap
    tmp = candidate[_min]

    candidate[_min] = L[inversion-1]

    L[inversion-1] = tmp

    return L[0:inversion] + sorted(candidate)


class Testing(unittest.TestCase):
    def test_happy_case(self):
        l = [6,2,1,5,4,3,0]
        self.assertEqual(next_perm([6,2,1,5,4,3,0]), [6,2,3,0,1,4,5])

if __name__== "__main__":
    unittest.main().result
