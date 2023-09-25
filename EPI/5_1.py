#! /usr/local/bin

import sys

def main():
    A = eval(sys.argv[1])
    index = int(sys.argv[2])


    p = A[index]

    lt = 0

    for i in range(0, len(A)):
        if A[i] < p:

            A[i] , A[lt] = A[lt], A[i]
            lt = lt + 1
    
    print(A)
    print("the last element < p  is {0} at index {1}".format(A[lt], lt))

    gt = len(A) -1

    for i in range(len(A)-1, 0 , -1):
        if A[i] > p:
            A[i], A[gt] = A[gt], A[i]
            gt = gt -1




    print ("pivot is {0} at index {1}".format(p, index))
    print(A)

    



if __name__=="__main__":
    main()



