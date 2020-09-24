#!usr/local/bin

import sys
import ast

if __name__=="__main__":

    a = ast.literal_eval(sys.argv[1])
    print a
    # there is an o(n) time and o(1) space solution

    # i think we first need to sort the array
    a.sort()
    # now that is sorted to keep it o(1) space
    # we need to swap elements
    free = 1
    for i in range(1, len(a)):
        if a[i] == a[i-1] and a[free]!= a[i]:
            # move to this spot the repeated entry
            free =  i
        elif a[free]!= a[i]:
            # move  "i" to free spot if free!= -1
            a[free] = a[i]
            free = i
        print a



    print a[0:free]
