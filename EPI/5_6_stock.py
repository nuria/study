#/usr/local/bin

import sys

def max_diff(A):
    print A
    if len(A) == 2:
        #(diff, buy, sell)
        return (A[1]-A[0], A[0], A[1])

    elif  len(A) < 2:
        return (0, A[0], 0)
    else:
        l = len(A)
        L_result = max_diff(A[0:l/2])
        R_result = max_diff(A[l/2:])
        # how about difference across arrrays
        # the fact that across subarrys the optimun difference is the max(R) - min(L)
        # is not obvious
        l_min = min(A[0:l/2]) 
        r_max = max(A[l/2:])
        diff = r_max - l_min
        
        if diff == max(L_result[0], R_result[0], diff):
            return (diff, l_min, r_max)
        elif L_result[0] == max(L_result[0], R_result[0], diff):
            return L_result
        else:
            return R_result

def main():
    A = eval(sys.argv[1])
    # brute force is to by and sell all days time n^2 
    # better than that we can
    # compute differences with the day after , then we ahve an array of differences
    print max_diff(A)



if __name__ =="__main__":
    main()
