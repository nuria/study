#!usr/local/bin
import sys

import math

def inner_square_root(_max, _min, n):
    tolerance = 0.05
    middle = (_max -  _min) *0.5
    middle = _min + middle
    print "max: {0}, min:{1}, middle:{2}".format(_max, _min, middle)

    if abs(middle* middle -n) < tolerance:
        return middle
    elif middle * middle < n:
        return inner_square_root(_max, middle, n)
    else:
        return inner_square_root(middle, _min, n)


def square_root(n):
    # square root can be bigger than the number if the number  <1
    if n >= 1:
        # solution is between [1,n/2]
        return inner_square_root(n, 1, n)
    else:
        return inner_square_root(1, n, n)



if __name__=="__main__":
    n = int(sys.argv[1])
    print square_root(n)
