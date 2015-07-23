#!/usr/local/bin/python

import sys


def main():
    '''
    Given a sorted array and a target value, return the index
    if the target is found. If not, return the index where
    it would be if it were inserted in order. There won't be duplicate values in the array.

    For example:

    [1, 3, 5, 6] with target value 5 should return 2.
    [1, 3, 5, 6] with target value 2 should return 1.
    [1, 3, 5, 6] with target value 7 should return 4.
    [1, 3, 5, 6] with target value 0 should return 0.

    make sure it works for arrays that are large enough

    Call like: python problem6.py 2 '1 2 3 4'
    '''

    def find_target(t, l, left_index):
        # binary search, we need to keep track of indexes,
        # just remember left and right index of the sublist in which we are looking

        size = len(l)
        if size == 1:
            if t == l[0]:
                # base case
                print str(left_index)
            else:
                if l[0] < t:
                    print left_index + 1
                else:
                    if left_index != 0:
                        print left_index - 1
                    else:
                        print 0
        else:
            # split in two
            middle = int(size/2)
            if l[middle] == t:
                print left_index + middle
            elif l[middle] > t:
                left = l[left_index:middle]
                find_target(t, left, left_index)
            elif l[middle] < t:
                    right = l[middle:size]
                    find_target(t, right, left_index + middle)

    target = sys.argv[1]
    l = sys.argv[2].split()

    find_target(target, l, 0)


if __name__ == "__main__":
    main()
