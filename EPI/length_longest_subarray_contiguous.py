#!/usr/local/bin

# Find the length of the longest continuous strictly increasing subarray in an integer array


def main():
    A = [1, 4, 9,2, 3, 6, 5,3,1, 5, 7, 8, 4, 2]
    
    # how do you do this by brute force?

    # try every sequence starting at every number, that would be o(n2)

    # how can we do better

    # well, not repeating looking at sequences we have alredy seen

    # if you start at i  number at i+n needs to be at least i + n 
    # you can keep moving the pointer from i but you will be doing a bunch of repeated comparations

    # p1 = 0 
    # p2 = end
    # if A[-1] > A[i] + ([0-end]) then longest is 0-end
    # move until you have a sequence, it could be that there is none
    # if seq is at distance say m , you know taht for elelemnt i +1 there is an incresing sequence up to m at least 
    # so we need to test m+1 and beyond

    i = 1
    p = 0
    max_l = 1
    while i < len(A)-1:
        if A[i] < A[i+1]:
            # continues to increase , update max_l if needed
            if (i+1 -p) > max_l:
                max_l = i +1 -p
        else:
            # it dip
            # start counting again
            p =  i + 1
        i = i + 1

    DP = [0 for i in range(0, len(A))]

    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            DP[i] = DP[i-1] +1
        else:
            DP[i] = 0




    
    print "maximun strictly increasingi while loop: {0}, dp :{1}".format(max_l, max(DP))

if __name__=="__main__":
    main()
