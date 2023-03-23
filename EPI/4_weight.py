#!/usr/bin

import sys

def main():
    n = int(sys.argv[1])

    # trick is to realize that it is not the 
    # swaping the LS 1 and LS 0 what works but rather swaping the 
    # two LSB that differ

    # assume 64 bits
    k = 0
    while k < 64:
        if (n >> k) & 1  !=  (n >> k +1) & 1:
            # these two bits give different results when & with 1
            # now we need to swap them 
            # using some mask 
            print 1 << k
            print 1 << k +1

            mask = (1 <<k) | (1 <<(k+1))
            x = n ^ mask
            print x
            break

        k = k + 1 



if __name__=="__main__":
    main()
