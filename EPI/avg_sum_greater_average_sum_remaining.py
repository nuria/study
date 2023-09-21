#!/usr/local/bin

"""
You are given an array A containing N integers. Your task is to find all subarrays whose average sum is greater than 
the average sum of the remaining array elements. You must return the start and end index of each subarray in sorted order.

outputs are indexes [R,L]  starting at 1 (why?)

premise of question implies subarray is contiguous

A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].

"""

import sys

def main():
    
    A = eval(sys.argv[1])

    # find all subarrays

    # we can start with a window of size 1 and after size 2 and move it arround until size is len(A)-1

    # w = [0:1] for 1st element rest is 1 A[1:]
    # we iterate on array on 'i' but also on size of window on w
    # we can use space and memorize intermediate results 

    result = [A]

    # k = size of window

    # sum prior subarray
    sum_prior_w = 0

    # sum prior rest 
    sum_prior_r = 0

    for k in range(1, len(A)):

        for i in range(0, len(A)-k):
            if i ==0:
                w = sum(A[0:k])
                r = sum(A[k:])
                if w/k > r/(len(A)-k):
                    # they ask for 1 indexing
                    result.append([A[0], A[0+k-1]])
            else:
                w = sum_prior_w + A[i + k -1] - A[i-k]
                r = sum_prior_r - A[i + k - 1] + A[i-k]
                if w/k > r/(len(A)-k):
                    result.append([A[i], A[i+k-1]])

            # this can be used to speed up the sums
            sum_prior_w = w
            sum_prior_r = r
            
    print(result)

if __name__=="__main__":
    main()



