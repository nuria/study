#!/usr/localbin/python
# execute like python blah.py "[1,4,6,0, 2]"

import sys
import ast

l  = ast.literal_eval(sys.argv[1])

def partition(l):
    if len(l) <= 1:
        return l

    p = l[0]
    i = 1
    for k in  range(1, len(l)):
        if l[k] <= p:
            tmp = l[i]
            l[i] = l[k]
            l[k] = tmp
            i = i + 1


    less = l[1:i]
    more = l[i:len(l)]

    print ("less: {0} and more {1} and i boundary {2}").format(less, more,i)
    return(partition(less) +[p] + partition(more))

map(int,l)
print l

print partition(l)
