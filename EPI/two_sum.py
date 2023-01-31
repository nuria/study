#!/usr/bin



def main():
    l = [6,7,89,34,5,7,2,1,2,3,45]
   
    l.sort()
    s =13
    # see if two items sum another one
    
    p1 = 0
    p2 = len(l) -1
    while p1 <p2:
        # walk the top part of the array 
        # until 1st candidate is found 
        while l[p2] > s:
            p2 = p2 -1
        # candidate sum 
        c = l[p1] + l[p2]
        if c ==s:
            print "{0} {1}".format(l[p1],l[p2])
            return
        elif c > s:
            # move p2
            p2 = p2 -1
        else:
            p1 = p1 +1


if __name__=="__main__":
    main()
