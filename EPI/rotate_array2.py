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
   
    buffer = A[l-k:]

    # we have a buffer of size k where the last k elements will go
    # we move other elements forward k steps
    # this is o(n) on time by o(k) on space
    
    for i in range(l-1-k, -1 , -1):
        A[i+k] = A[i]


    for i in range(0, k):
        A[i] = buffer[i]

    print(A)


   

if __name__=="__main__":
    main()
