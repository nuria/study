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
    k = sys.argv[2]

    # brute force will move all N elements K times
    # o(k) in terms of time but O(Nk) in terms of space so bound is o(N2) if k=N
    # best solution has to do it in place
    # [1,2,3,4,5,6,7]
    # iteration is [7,2,3,4,5,6,1]
    # [2,7,3,4,5,6,1]
    # [2,7,3,4,5,1,6]
    # [6,7,2,3,4,5,1,2]
    
    # so switch N with 0 element
    # do the following as many times as swaps we have done
    # swap 0 element with 1
    # swap N element with N-1

    # two pointers
    p1= 0
    l = len(A) - 1
    p2 =l
    p = 0

    while p <k:
        tmp = A[l]
        A[l] = A[0]
        A[0] = tmp
        
        p1 = p1 + 1
        
        p2 = p2 -1
        print A

        if p1 < k:
            for i in range(p1, 0, -1):
                # now move forward
                # swap element at p1 with p1-1 until we get back to 0
                tmp = A[i]
                A[i] = A[i-1]
                A[i-1] = tmp
        
        print A

        for j in range(p2, l):
            tmp = A[j +1]
            A[j+1] = A[j]
            A[j] = tmp
        
        p = p + 1
        
        print A


    print " rotating array {0} steps : {1}".format(k, A)

if __name__=="__main__":
    main()
