#!usr/local/bin
import sys

"""
if input is 1101 output is 1011, program should work for 8 bit integers
"""
cache = {}

# simulation with 8 bits

# looks like we need to make these keys strings
cache['0b0'] = 0b00
cache['0b1'] = 0b10
cache['0b10'] = 0b01
cache['0b11'] = 0b11


if __name__=="__main__":
    n = int(sys.argv[1])

    # split in two bit chucks
    mask = 0b11

    print bin(n)

    mask_size = 2
    c1 = (n >> 3 * mask_size) & mask
    c2 = (n >> 2* mask_size) & mask
    c3 = (n >> mask_size) & mask
    c4 =  n & mask

    print bin(c1)
    print bin(c2)
    print bin(c3)
    print bin(c4)

    n =  cache[bin(c4)] << 3* mask_size | cache[bin(c3)] << 2 * mask_size | cache[bin(c2)] << mask_size | cache[bin(c1)]

    print bin(n)




