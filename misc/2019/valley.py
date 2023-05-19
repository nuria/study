#!/bin/python

import os
# Complete the countingValleys function below.
def countingValleys(n, s):
    _steps = list(s)
    steps = [1 if item == "U"  else -1 for item in _steps ]
    def change(x):
        if x == "U":
            return 1
        else:
            return -1

    #steps = map(change, _steps)
    valleys = 0

    i = 0

    while i < n:
        # go through the loop
        # until the amount sums 0, if it starts with -1 it is a valley
        _sum = steps[i]
        if steps[i] < 0:
            valley = True
        else:
            valley = False
        k = i
        while _sum != 0 and k < n:
            k = k + 1
            _sum = _sum + steps[k]

        # since int(True) => 1
        valleys = valleys + int(valley)
        i = k + 1

    return valleys



import sys

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')

    n = f.readline()

    s = f.readline()

    result = countingValleys(int(n), s)

    print ("valleys: {0}").format(result)


