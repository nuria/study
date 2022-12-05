#!usr/bin

import sys
_input = sys.argv[1]

def main():
    f = open (_input)
   # In how many assignment pairs does one range fully contain the other?
   # this seems like sets
   # if the intersection of the two equals one of them 
    counter = 0
    for l in f:
        l=l.strip()
        (p1, p2) = l.split(',')
        #print "{0}, {1}".format(p1,p2)
        (s1,e1) = p1.split('-')
        s1 = make_set(int(s1), int(e1))
        (s2,e2) = p2.split('-')
        s2 = make_set(int(s2), int(e2))
        #print s1
        #print s2

        if (len(s2.intersection(s1))!=0):
            counter = counter + 1
           # print "intersection"

    print "counter"
    print counter


def make_set(s,e):
    return set([i for i in range(s,e+1)])



if __name__== "__main__":
    main()
