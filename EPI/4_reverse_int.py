#!usr/local/bin
import math
import sys

def reverse_no_string(n):
    # array of numbers
    digits = []

    r = 0
    while ((n /10) >1):
        remainder = n % 10
        digits.append(remainder)
        n = n/10

    digits.append(n)
    print digits

    l = len(digits)

    for d in digits:
        r = r + math.pow(10, l-1) * d
        l = l -1
    return r


if __name__=="__main__":
    n = int(sys.argv[1])
    print reverse_no_string(n)
