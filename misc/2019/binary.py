#!/usr/local/bin/python
# binary search find an aitem on a sorted array
# call program like python binary.py "[1,2,3]"

import sys
import ast

def split(l):
    m = len(l)/2
    first = l[0:m]
    second = l[m : len(l)]
    return first, second

def contains(l,c):
    if len(l) == 1:
        if l[0] == c:
            return True
        else:
            return False

    # split array
    first, second = split(l)
    if c>=second[0]:
        return contains(second,c)
    else:
        return contains(first,c)

l = ast.literal_eval(sys.argv[1])
l = map(int,l)

c = int(sys.argv[2])

print ("looking whether {0} contains {1}".format(l,c))

print contains(l,c)
