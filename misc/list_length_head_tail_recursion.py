#!/usr/local/bin

import sys


def len_head_r(l):
    # last is equal to 1st
    # we only have 1 element
    if l[-1] == l[0]:
        return 1
    else:
        return 1 + len_head_r(l[1:])



def len_tail_r(l, acu= 0):
    if l[-1] ==l[0]:
        return 1+ acu
    else:
        return len_tail_r(l[1:], acu +1)
    


def main():
    l = [ i for i in range(0, 1000)]

    print len_head_r(l)
    print len_tail_r(l)




if __name__=="__main__":
    main()
