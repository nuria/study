#!/usr/local/bin
# -*- coding: utf-8 -*-
# h index measure of productivity and and citation impact of a researcher
# largest number of h such there are h papers that have been published h times
# ex: A,B,C,D,E,F,G,H papers which have been cited 1,4,1,4,2,1,3,5,6
# h index is 4 corresponding to B,D,H,I

def main():
    l = [1,4,1,4,2,1,3,5,6]
    # we can probe
    # sort list 
    # build data structure ¶
    # or rather add to a hash
    # 1 -> 9
    # 2 -> 6
    # 3 -> 5
    # 4 -> 4
    # 5 _>2
    # 6->1
    # this works but it is o(n) space 

    # seems like this could benefit from sorting 
    # brute force
    # number of papers with these number of citations
    c = {}
    
    l.sort()

    _max = 0
    tally = 0

    # [6,5,4,4,3,2,1,1,1]
    for n in reversed(l):
        if c.get(n) is None: # 
            c[n] = tally + 1
        else:
            c[n] += 1
        tally = tally + 1

        if c[n] == n and n > _max:
            _max = n

    print _max



if __name__=="__main__":
    main()
