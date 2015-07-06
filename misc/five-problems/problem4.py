#!/usr/local/bin/python
'''
Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.
Invoque like: python problem.py '1 2 3'
'''
import sys


def main():
    def sort_max(l1, l2):
        '''
        We can sort as text and if two numbers start with the same one we return
        reverse integer sorting
        '''
        # get first digit
        li1 = int(l1)
        li2 = int(l2)

        if l1[0] == l2[0]:
            # reverse integer
            if li1 > li2:
                return -1
            else:
                return 1
        else:
            # natural string sort
            if l1 < l2:
                return -1
            else:
                return 1

    l = sys.argv[1].split()
    l.sort(sort_max)
    print l
    l.reverse()
    print "".join(l)

if __name__ == "__main__":
    main()
