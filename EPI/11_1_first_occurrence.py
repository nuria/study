#/usr/bin
#search a sorted array for the 1st ocurrence of k
# and return its index

import sys

def main():
    A = eval(sys.argv[1])

    # target
    t = eval(sys.argv[2])
    # binary search but carrying the index?

    top = len(A)
                
    bottom = 0
    

    while bottom < top:
        m = bottom + (top-bottom)/2
        print "top:{0}, bottom:{1}".format(top, bottom)
        L = A[bottom: m]
        R = A[m:top]

        print L
        print R

        if A[m] == t:
            # we are split down the middle
            while A[m-1] == t and m-1 >0:
                m = m-1
            print "We found {0} at lowest index : {1}, {2}".format(t,m, A[m])
            return

        if L[-1] < t:
            # continue on right
            bottom = m
            top = len(A)
        elif R[0] > t:
            # continue on left
            top = m
            bottom = 0



if __name__=="__main__":
    main()
