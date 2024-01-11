#!/usr/local/bin

import sys

def main():
    # find maximun subarray, average sum of subarray 
    # [-2,1,-3,4,-1,2,1,-5,4] => 6 with subarray [4,-1,2,1]

    A = eval(sys.argv[1])

    _max = 0

    # the brute force solution is calculting all arrays 
    # DP?
    DP = []
    # rows: i 0 -len(A)
    DP = [[0] * (len(A)+1) for i in range(0, len(A)+1)]
    
    # first row is the array itself
    #DP[i][j] => array that starts at i of length j, some of the matrix will be empty
    
    _sum = float('-inf')
    
    a = 0 
    b = 0
    for i in range(0, len(A)):
        DP[i][1] = A[i]
        if A[i]> _sum:
            _sum = A[i]
            a = i
            b = i
    
    # this is still o(n2)
    # dp like but not really cause we are computing every single sum
    # is this the right DP ? seems very explicit

    for i in range(0 ,len(A)):
        for j in range(2,len(A)-i):
            # array that starts at i of length j
            # if adding the new element makes sum go up great
            # otherwise no need to keep that value
            # first will be DP[0][2]
            if A[j-1] + DP[i][j-1] > DP[i][j-1]:
                DP[i][j] = DP[i][j-1] + A[j-1]
                if DP[i][j]> _sum:
                    _sum = DP[i][j]
                    a = i
                    b = j
            else:
                # do not consider this length not lengths that are bigger that 
                # start at i 
                DP[i][j] = DP[i][j-1] + A[j-1]

    print("sum: {0}  subarry: {1}". format(_sum, A[a:a+b]))


if __name__=="__main__":
    main()
