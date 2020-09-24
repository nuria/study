#!usr/local/bin/python
import sys

if __name__=="__main__":
    n = int(sys.argv[1])

    # find the closest number with equal weight
    # well stands to reason that first we need to find the weight?
    # this is finiding how many bites are set to 1
    # the number is the one with the right most bit set to 1
    # so find which is the right most bit set to zero

    # find the right most 01 or 10 and flip it

    #01 & 1 = 01 and 01 & 0 = 00
    #10 & 1 =  1

    print bin(n)

    for i in range (64-1):
        # shift as many bits and see if i and i+1 differ
        if (n >> i) & 1 != (n>> i+1) & 1:
            n = n ^ (1 << i)
            n = n ^ (1 << i+1)
            break
    print n
    print bin(n)
