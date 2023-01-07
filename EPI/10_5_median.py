#!/usr/local



import heapq as h

import sys


def main():

    _input = eval(sys.argv[1])

    # median onwards
    # min heap
    H = list()

    # less than median
    # max heap
    L = list()

    # initialize heaps 
   # maybe this is not needed but makes this easier
   # although makes program stateful
    
    h.heappush(L, (-1)*_input[0])
    m = _input[0]
    print "input :{0} mean {1}".format(_input[0], m)

    for n in _input[1:]:
        if n  <= m:
            # incoming item is smaller than smallest before mean
            h.heappush(L , (-1) *n)
        elif n >= m:
            h.heappush(H, n)
        
        if abs(len(H) - len(L))  >= 2:
            # move elements arround before doing anything
            if len(H) > len(L):
                # we should only need to move one element
                h.heappush(L, (-1) * h.heappop(H))
            else:
                h.heappush(H, abs(h.heappop(L)))


        print L
        print H
        # now we are computing median like
        if len(H) == len(L):
            m = (abs(L[0]) + H[0])/2.0
        else:
            m = abs(L[0])
        print "input: {0}, mean:{1}".format(n, m)






if __name__=="__main__":
    main()
