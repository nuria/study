#/usr/bin

import sys
import random

# divides array arround a random pivot and sorts
def _sort(A, K):
    if K  > len(A):
        print "error"
        return -1
    
    if K == 0 and len(A) <=2:
        return min(A)
    elif K == 1 and len(A)  <= 2:
        return max(A)

    r = random.randint(0, len(A)-1)
    p = A[r]
    left = []
    right = []
    # this can be done in place as well
    for i in range(0, len(A)):
        if A[i] <=p:
            left.append(A[i])
        else:
            right.append(A[i])
    
    print "pivot:{0}, left:{1}, right: {2}, k: {3}".format(p,left, right,K)

    # now recurse just in one side
    # we are ordering smaller to largest
    if K >= len(left):
        # k largest is at right 
        return _sort(right,K-len(left))
    else:
        # k largest is on left array
        return _sort(left,K)


def main():
    A = eval(sys.argv[1])
    K = eval(sys.argv[2])

    # kth largest element 
    #  element at index k-1 when sorted descending
    # obvious => sort and pick k which is nlogn in time

    # let's just not have to deal with zero indexing
    result = _sort(A, K-1)
    print result


if __name__=="__main__":
    main()
