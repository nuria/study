#!/usr/local/bin
"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
input = 145852-616942

"""
from collections import Counter

def isDecreasing(n):
    l = list(str(n))
    l.sort()

    return "".join(l) == str(n)


def hasAdjacent(n):
    l = list(str(n))

    d = Counter(l)

    for i in range(0, len(l)-1):
        if l[i] == l[i+1] and d[l[i]] == 2:
            return True
    return False

if __name__ == "__main__":
    c  = 0
    for n in range(145852, 616942 +1):
        if hasAdjacent(n) and isDecreasing(n):
            print n
            c = c +1

    print c
