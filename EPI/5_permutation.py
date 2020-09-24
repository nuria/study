#!usr/localbin/python
import unittest



def perm_one_pass(l):
    # find the first entry from the right that is smaller than the entry imediately after it
    inversion_point  = len(l) -2
    while(inversion_point >= 0 and l[inversion_point] >= l[inversion_point + 1 ]):
        inversion_point = inversion_point -1

    # check for last
    if inversion_point ==-1:
        return []

    # we know the entry that needs to be swapped , it is inversion_point + 1
    # swap that entry by the smallest one on the suffix
    # from the right find entry that is larger
    for i in range(len(l)-1, inversion_point-1, -1):
        print "testing"
        print "{0} > {1}".format( l[inversion_point], l[i])
        if l[i] > l[inversion_point]:
            tmp = l[inversion_point]
            l[inversion_point]  = l[i]
            l[i] = tmp
            break

    l[inversion_point + 1:] = sorted(l[inversion_point + 1:])

    return l


class testing(unittest.TestCase):
    def test_happy_case(self):
        next_p = perm_one_pass(['1','0','3','2'])
        self.assertEquals(['1','2','0','3'],next_p)

    def test_short_list(self):
        next_p = perm_one_pass(['1','2'])
        self.assertEquals(['2', '1'], next_p)

    def test_larger_list(self):
        next_p = perm_one_pass(['1','1', '1', '1', '2'])
        self.assertEqual(['1', '1', '1', '2', '1'], next_p)

    def test_happy_case2(self):
        next_fast_p = perm_one_pass([6,2,1,5,4,3,0])
        self.assertEqual([6,2,3,0,1,4,5], next_fast_p)


if __name__=="__main__":

    unittest.main().result
