#!/usr/bin

import sys
import string



def main():
    
    _file = sys.argv[1]

    f = open (_file)

    repeated = []

    for l in f:
        sack = l.strip()
        c1 = set(sack[0:len(sack)/2])
        c2 = set(sack[len(sack)/2:len(sack)])
        item = c1.intersection(c2).pop()
        # now find the character that appears in c1 and c2
        repeated.append(item)

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
