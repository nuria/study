#!/usr/local

import sys





def  in_order(left, right, next_left=None, next_right=None):
    
    # two ints
    if not isinstance(left, list) and not isinstance(right,list): 
        # integer comparison
        if left > right:
            return False
        else:
            return in_order(next_left, next_right)
    
    # mixed case
    if not isinstance(left, list) and isinstance(right, list):
        # left is an integer
        return in_order(eval("["+str(left)+"]"), right, next_left, next_right)

    elif (isinstance(left, list) and not isinstance(right, list)):
        return in_order(left, eval("["+str(right)+"]"), next_left, next_right)

    # list case 
    if len(left) > len(right):
        # no need to check elements left list is bigger than right
        # so bad order
        return False
    elif len(left) == len(right):
        if len(left) >0:
            # both lists are at least of length 1
            l = left.pop(0)
            r = right.pop(0)
            
            return in_order(l, r,left, right)
        else:
            # empty lists
            return True
    else:
        # left < right
        # good order , keep on checking
        if len(left) > 0:
            
            l = left.pop(0)
            r = right.pop(0)
            return in_order(l, r,left, right)
        else:
            # left side run out of items
            return True

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

    print pairs

    order = []
    
    # build for each tuple
    for i  in range(0, len(pairs)):
        p = pairs[i]
        left = eval(p[0])
        right =eval(p[1])

        if in_order(left, right):
            order.append(i+1)

    print "pairs in order"
    print order
    print sum(order)

if __name__=="__main__":
    main()
