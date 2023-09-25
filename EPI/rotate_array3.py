#!/usr/local/bin
"""
nums = [1,2,3,4,5,6,7], k = 3
rotate nums array k steps
output: [5,6,7,1,2,3,4]
"""
import sys 

def main():
    

    A = eval(sys.argv[1])
    k = int(sys.argv[2])

    l = len(A) 
   
    
    # we can also swap element i with next element l-k times
    

    n = 0

    # swap with neighbor all the way up to end 
    # l - k times 
    while n < l-k:
        # move A[0] l-k steps forward
        j = 1 
        while (j < l):
            
            A[j], A[j-1] = A[j-1], A[j]

            j = j + 1

        n = n + 1
    print (A)
   

if __name__=="__main__":
    main()
