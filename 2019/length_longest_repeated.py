#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
"""
// Find the length of the longest repeated substring that is inside of a string
//
// Example 1:
// “AAAA” has 2 repeats of “AAA":  (AAA)A and A(AAA)
//  the length of the repeated string is 3
//
// Example 2:
// "Oh toil toil toil trouble” has two repeats of " toil toil t"
// Oh ( toil toil t)oil trouble” and  “Oh toil( toil toil t)rouble”.
// The length of the repeated substring is 12


//ABCDEABC -> return 3
// A -> 0
// AA -> 1
// AB -> 0
"""
import sys



def main():
    
    s =  sys.argv[1]
    print "looking for matches for {0}".format(s)
    window_lengths= [i for i in reversed(range(1, len(s)))]
    #print window_lengths 
    
    # slide window on original string starting with largest window

    for l in window_lengths:
        i = 0
        while i + l < len(s):
            w = s[i:i+l]
            # now  compare this with original string and see if there is more than 1 match
            match = 0
            for k in range(0, len(s)):
                #print "comparing: {0} and {1}".format(w, s[k:k+l])
                if k+l <=len(s) and w == s[k:k +l]:
                    match = match + 1
                if match > 1:
                    print " {0} matches for string : {1}".format(match, w)
                    # we are going in reverse order, 1st match found is the longest
                    return 
            i = i +1


if __name__=="__main__":
    main()

