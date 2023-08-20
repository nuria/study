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

    Call like: python problem6.py 2 '1,2,3,4'
    '''
    target = int(sys.argv[1])
    A = eval(sys.argv[2])

    # let's use binary search to start 
    # first we need to stablish if item is on array
    
    U = len(A) -1
    L = 0

    # let's get the ones out of bounds
    if target > A[-1]:
        print(len(A))
        return
    if target < A[0]:
        print ("0")
        return

    while (U > L):
        m = L + int((U-L)/2)
        print("U:{0} L:{1}".format(U,L))

        if target > A[m]:
            # move right
            # look ahead and see see if the next value is out of bounds
            if m < len(A)-1:
                if target < A[m+1]:
                    print(m)
                    return
                else:
                    L = m
        elif target < A[m]:
            if m > 0:
                if target > A[m-1]:
                    print(m)
                    return
            else:
                U = m
        else:
            print(m)
            return




if __name__=="__main__":
    main()
