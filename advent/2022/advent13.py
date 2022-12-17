#!/usr/local

import sys



def  in_order(left, right):

    print "left: {0}, right:{1}".format(left, right)

    # two ints
    if type(left) ==int  and type(right)==int: 
        # integer comparison
        if left > right:
            return -1
        elif left < right:
            return 1
        else:
            return 0


    # mixed case
    if type(left)==int and not type(right)==int:
        # left is an integer
        return in_order([left], right)

    elif not type(left)==int and type(right)==int:
        return in_order(left, [right])

    for l, r in zip(left, right):
        if in_order(l,r)  < 0:
            return -1
        elif in_order(l,r) > 0:
            return 1


    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0




def main():
    f = open(sys.argv[1])
    pairs = []
    l1 = None
    l2 = None
    for l in f:
        l = l.strip()
        if l == "":
            pairs.append((l1,l2))
            l1 = None
            l2 = None
        else:
            if l1 is None:
                l1 = l
            else:
                l2 = l

    #print pairs

    order = []
   

    #print pairs[9][0]
    #print pairs[9][1]
    # build for each tuple
    for i  in range(0, len(pairs)):
        p = pairs[i]
        left = eval(p[0])
        right =eval(p[1])

        if in_order(left, right) >0:
            order.append(i+1)

    print "pairs in order"
    print order
    print sum(order)

if __name__=="__main__":
    main()
