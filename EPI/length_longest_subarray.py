#!/usr/local/bin

# Find the length of the longest continuous strictly increasing subarray in an integer array
# with one chnage allowed

"""
Step 1: We first compute the longest increasing subarray ending at an index for every index in the given array. We store these values in l[].
Step 2: Then calculate the longest increasing subarray starting at an index for every index in the given array. We store these values in r[].
Step 3: Update the answer ans = max ( ans, l[i-1] + r[i+1] + 1), when a[i-1] + 1 < a[i+1].
"""


def main():
    A = [1, 4, 9,2, 3, 6, 5,3,1, 5, 7, 8, 4, 2]
    A = [7,2,3,1,5,10 ]

    i = 1
    p = 0
    max_l = 1
    
    



    # stores longest sequence finishing at index i
    DP = [1 for i in range(0, len(A))]
    
    # stores longest sequence starting at index i
    DP_S = [1 for i in range(0, len(A))]

    # counts length of sequence
    p = 1
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            p = p + 1
            DP[i] = DP[i-1] + 1
        else:
            p = 1


    for i in range(len(A)-2, -1, -1):
        # populate DP_S backwards
        # from DP
        # stores longest sequence starting at index i
        if DP[i+1] > DP[i]:
            DP_S[i] = DP_S[i+1] + 1
        else:
            # jump
            DP_S[i] = 1


    print DP_S
    print DP

    # now we have the longest that finishes at i plus longest that starts at i 

    max_l = max(DP)
    for i in range(1, len(A)-1):
        if DP[i] + DP_S[i+1] > max_l and A[i] < A[i+2]:
            max_l = DP[i] + DP_S[i+1]

    
    print "maximun increasing with one change : {0}".format(max_l)

if __name__=="__main__":
    main()
