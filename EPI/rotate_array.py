#/usr/bin
"""
nums = [1,2,3,4,5,6,7], k = 3
rotate nums array k steps 
output: [5,6,7,1,2,3,4]
"""
import sys
import copy

def main():
    
    A = eval(sys.argv[1])
    k = int(sys.argv[2])

    # brute force will move all N elements K times
    # o(k) in terms of time but O(Nk) in terms of space so bound is o(N2) if k=N
    # best solution has to do it in place
    # this is not a two pointers sort of problem
    #  1st let's do teh obvious one taht is not brute force

    l = len(A) -1
    while k > 0:
        # move to the right

        for i in range(len(A)-1, 0, -1):
            tmp = A[i-1]
            A[i-1] = A[i]
            A[i] = tmp
        print A
        k = k -1



    print " rotating array {0}".format(A)

if __name__=="__main__":
    main()
