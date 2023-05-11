#!/usr/local/bin

import sys

def main():
    A = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    key = int(sys.argv[1])

    # find low and high index of a key, array is sorted
    # binary search for high and low?
    # no, binary search for one and once that is found just look ahead
    # that would be log(N)

    # you can O(n) space and do a hashmap lookup

    def low_index(key):
        U = len(A) - 1
        L = 0

        m = L + (U-L)/2

        while U > L:
            i = m
            print "upper: {0}, lower: {1}, middle: {2}, A[middle]: {3}, key:{4}".format(U, L, m, A[m], key)
            if A[i] < key:
                # look if we found low
                if i + 1 < len(A) and A[i+1] == key:
                    return i+1
                else:
                    # move forward L
                    L = i + 1
            elif A[i] > key:
                if i -1 > 0 and A[i-1] == key:
                    # this is the high index
                    if i-2 > 0 and A[i-2] != key:
                        #high and low is same
                        return i-1
                    else:
                        U = i -1
                else:
                    # move back
                    U = i
            elif A[i] == key:
                if i - 1 > 0 and A[i-1] != key:
                    return i
                elif i == 0:
                    return i
                elif i -1 > 0 and A[i-1] == key:
                    U = i - 1

            m = L + (U-L)/2

    print "looking for low index for: {0}".format(key)
    li = low_index(key)
    print "low index: {0}".format(li)
    
    hi = len(A) -1

    # once you have the low index is easy to find the high one
    for i in range(li, len(A)):
        if A[i] != key:
            hi = i -1
            break

    print "high index: {0}".format(hi)





if __name__=="__main__":
    main()
