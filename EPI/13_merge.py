#/usr/local/bin

# merge two sorted arrays
# updates first array to the combined entries of the two arrays in sorted order
# first array has enough entries at the end to hold the result
# hint: avoid repetedealy moving entries

# mover forward from index i, 1 position
# we know there is space after index j
import unittest




def merge(a,b, n):
    # rememeber, zero based indexing
    # assume there is space
    write_index = n + len(b) -1

    # we process the arrays starting from the back
    # two indexes, one for a , one for b
    i = n - 1
    j = len(b) - 1

    while write_index >0:
        if b[j] >= a[i]:
            # enter item from b
            # at the end
            a[write_index] = b[j]
            j = j -1
        else:
            # enter item from a
            a[write_index] = a[i]
            i = i -1

        write_index = write_index- 1
        print a

    return a


class testing(unittest.TestCase):

    def  test_merge(self):

        c = merge([3,13,17,'-','-','-','-','-'],[3,7,11,19], 3)
        self.assertEqual(c, [3,3,7,11,13,17,19,'-'])

if __name__=="__main__":
    unittest.main().result
