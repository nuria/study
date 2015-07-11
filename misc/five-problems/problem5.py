#!/usr/local/bin/python

import sys


def main():

    l = sys.argv[1].split()
    total = int(sys.argv[2])

    '''
    Write a program that outputs all possibilities to put + or - or nothing between
    the numbers 1..9 (in this order) such the result is always 100
    1 + 2 + 34 -5 + 67 - 8 + 9
    Call program like: python problem5.py '1 2 3 4' '11'
    '''
    cache = []

    def build(l, total, signature):
        '''
        l is a list of integers
        total is the number we are shooting for
        signature is a string like '4 + 56'
        that we will evaluate
        '''
        if len(l) == 2:
            # base case
            #print "l[0] {0} l[1] {1} total {2}".format(l[0], l[1], total)
            if l[0] == total - l[1]:
                signature = signature + "+" + str(l[0]) + "+" + str(l[1])
                cache.append(signature)
                #print "valid"
            elif l[0] == total + l[1]:
                signature = signature + "+" + str(l[0]) +"-" + str(l[1])
                cache.append(signature)
                #print "valid"
            #else:
                # not a valid solution, what do we do?
                #print "not valid"
        else:
            # more than 2 numbers, keep recursing, trying different possibilities
            # for grouping
            for i in range(1, len(l)-1):
                digits = ''
                for t in range(0,i):
                    digits = digits + str(l[t])
                build(l[i:], total - int(digits), signature + "+" + digits)
                build(l[i:], total + int(digits), signature + "-" + digits)

    build([int(x) for x in l], total, '')

    # loop through cache solutions whose total is
    # what we want
    for key in cache:
            print key
            print eval(key)
if __name__== "__main__":
    main()
