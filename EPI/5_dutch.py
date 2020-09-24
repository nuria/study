#!/usr/local/lib


def happy_partition(A, i):
    # it is easy to do this in o(n) space allocating another array
    # now, let's do it in o(1) space
    p = A[i]
    # index to loop through array
    n = 1
    # index to keep track of where is the pivot at
    i = 0
    # index to keep track where "equal" zone ends
    j =  0

    # move pivot at the beginning of array
    tmp = A[0]
    A[0] = A[i]
    A[i] = tmp

    while n < len(A):
        # loop through all entries
        if A[n] == p:
            j = j + 1
            tmp = A[j]
            A[j] = A[n]
            A[n] = tmp
        elif A[n] < p:
            # swap pivot
            A[i] = A[n]
            # update pivot index
            i = i + 1
            j = j + 1
            tmp = A[j+1]
            A[j+1] = p
            A[n] = A[j+1]
        n = n + 1
    return A


if __name__=="__main__":
    A = [0,1,2,0,2,1,1,3,5,6]
    # write  aprogram that takes an array A and an index i into A (p = A[i]) and rearranges the elements such
    # all elements < p appear first, after there are teh 'p' elements and later >p
    print happy_partition(A,2)

