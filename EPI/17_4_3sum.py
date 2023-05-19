#!/usr/bin

import sys

# finds entry k in array A 
def find(k,A):
    b = 0
    t = len(A) -1

    if not(A[b] <= k and  A[t] >= k):
        return False
   

    while b < t:

        m = b + (t-b)/2
        
        if k== A[m]:
            return True
        
        if k < A[m]:
            t = m - 1
        else:
            b = m + 1 
        

    return  False
    


def main():
    l = eval(sys.argv[1])
    n = eval(sys.argv[2])
    # see if there are three entries, not necessarily distinct 
    # which add up to this n number

    l.sort()
    print l

    for i in l:
        for j in l:
            if find(n-(i+j), l):
                print "{0}, {1}, {2}".format(i,j, n -(i+j))


if __name__=="__main__":
    main()
