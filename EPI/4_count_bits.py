#!usr/local/bin/python
import sys
# count the number of bits that are set to 1 in a nonnegative integer

def count_bits(n):
    bits = 0

    while n >0:
        bits = bits + (n & 1)
        n = n  >> 1

    return bits

def parity(n):
    cardinal = 0
    while n >0:

        cardinal += n & 1
        n = n >> 1
    return cardinal % 2




# since x & (x-1) equals x with its lowest SET bit erased

def parity_improved(n):
    # instead of doing n & 1
    bits = 0
    while n>0:
        bits = bits + 1
        # we would loop through here as many times as there are bits
        n = n & (n-1)

    return bits % 2





if __name__=="__main__":
    n = int(sys.argv[1])
    print count_bits(n)

    print parity(n)
    print parity_improved(n)


