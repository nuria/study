#!/usr/local/bin

import sys


def main():
    A = eval(sys.argv[1])
    k = int(sys.argv[2])
    # contiguous subarray with maximun average sum of length k 
    # call like: python max_average_sum_contiguous_subarray.py '[12,-5,-6,50]' 4

    _max = sum(A[0:k])
    # start moving window at k
    w = A[0:k]

    for i in range(k, len(A)):
        candidate = _max - A[i-k] + A[i]
        if candidate > _max:
            _max = candidate 
            w = A[i-k+ 1:i+1]
    
    print("sum:{0}, window:{1}".format(_max/k, w))



    # harder version of this problem is when the array can have length k or larger 
    # sol is here but very counter intiutive 
    # you can extend this solution adding space a la dynamic programing
    # M [0][k] -> keps the sum of [0:k] so when we have to calculate 0:k+1 is available
    # so we need to keep space of o(N/K) , we can delete as we go   




if __name__=="__main__":
    main()
