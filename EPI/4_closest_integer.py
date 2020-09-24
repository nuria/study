#!usr/local/bin/python

# find closest integer with the same weight
# Weight is the number of integers that are set to 1
# in its binary form
import sys


if __name__=="__main__":
    n = int(sys.argv[1])

    print bin(n)

    # swap the two right most bits that differ
   # just doing 8 bits
    m = 0
    for i in range(0,7):
        # do bits differ
        if ((n >>i & 1) != (n>> (i+1) &1)):
            # if so swap them
            mask =  1 << i | 1 <<  i+1
            m = n ^ mask
            break

    print m
    print bin(m)
