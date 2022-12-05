#!/usr/bin

import sys
import string



def main():
    
    _file = sys.argv[1]

    f = open (_file)

    repeated = []

    # same deal but reading groups of 3

    _input = []
    for l in f:
        _input.append(list(l.strip()))

    i = 0
    while i < len(_input):
        c1 = set(_input[i])
        c2 = set(_input[i +1])
        c3 = set(_input[i+2])
        
        tmp = c1.intersection(c2)
        item = c3.intersection(tmp).pop()
        repeated.append(item)
        i = i + 3



    # build priority list
    alphabet = list (string.ascii_lowercase) + list(string.ascii_uppercase)
    PRI = {}
    
    print "repeated chars"
    print repeated
    
    p = 0
    for l in alphabet:
        PRI[l] = p + 1
        p = PRI[l]

    priority = 0
    

    for r in repeated:
        priority = priority + PRI[r]

    print "priority sum"
    print priority





if __name__== "__main__":
    main()
