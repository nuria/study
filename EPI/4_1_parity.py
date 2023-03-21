#/usr/local/bin

import sys

def main():
    # parity of a number is 1 if number of 1s in number is odd
    # 0 otherwise

    # easiests but o(n) on number of bits
    bits = 0
    n = eval(sys.argv[1])
    x = n

    while n > 0:
        if n & 1 == 1:
            bits +=1
        n = n >> 1

    if bits % 2:
        print "1"
    else:
        print "0"

    
    def compute_parity(x):
        
        bits = 0
        while x > 0:
            x = x & (x-1)
            bits+= 1
    
        if bits % 2:
            return 1
        else:
            return 0

    def divide(x):
        size = 16 
        mask = 0xFFFF
        
        # the  shift leaves us with 16 bits
        g1 = x >>(16 *3) 

        # the second shift needs a mask
        g2 = x>> (16*2) & mask
        
        # the third shift 
        g3 = x >> 16  & mask 

        g4 = x  & mask

        return [g1,g2,g3,g4]

    # parity is asociative, this computation can be divided in chuncks
    cache = {}

    # divide int in 4 groups
    
    groups = divide(x)
    
    print groups

    parity = 0

    for g in groups:
        if cache.get(g)  is None:
            cache[g] = compute_parity(g)
            
        parity = parity + cache[g] 
    
    if parity % 2:
        print "1"
    else:
        print "0"

    print cache


if __name__=="__main__":
    main()
