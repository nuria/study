#!/usr/local/bin/python
'''
Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.
Invoque like: python problem.py '1 2 3'

Good test case;  python problem4.py ' 5 2 1 9 50 56'

'''
import sys


def main():
    def sort_max(l1, l2):
        '''
        We can sort as text and if two numbers start with the same one we return
        reverse integer sorting unless they have the same number of digits
        '''
        # get first digit
        li1 = int(l1)
        li2 = int(l2)

        if l1[0] == l2[0]:
            if len(l1) == len(l2):
                # regular integer sort
                if li1 > li2:
                    return 1
                else:
                    return -1
            else:
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
