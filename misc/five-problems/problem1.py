#!/usr/local/bin/python

'''
Write three functions that compute the sum of the numbers
in a given list using a for-loop, a while-loop, and recursion.
'''
import sys

def main():

    # careful! first element of list is the program itself
    l = sys.argv[1:]

    def sum_for():
        total = 0
        for item in l:
            n = int(item)
            total = total + n
        return total

    def sum_w():
        total = 0
        cl= l[0:]
        while len(cl) > 0:
            n = int(cl.pop())
            total = total + n
        return total

    def sum_r(total,cl):
        if len(cl) > 0:
            total = total + int(cl.pop())
            return sum_r(total, cl)
        else:
            return total


    print sum_w()
    print sum_for()
    cl = l[0:]
    print sum_r(0, cl)

if __name__== '__main__':
    main()

