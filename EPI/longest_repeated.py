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
    # by definition the max length can only be len(S) -1
    # so start with the largest window, first match is the largest 
    match_length = len(s) -1

    i = 0
    
    while match_length > 0:
        #starting at 0
        # look for 0;len(s)-1 and after 1:len(s)
        for i in range(0, len(s) - match_length + 1):
            # so first values for i should be 0, 1
            candidate = s[i:i + match_length]

            for j in range(0, len(s) - match_length):
            
                if s[j:j + match_length] == candidate and j!=i:
                    
                    print " match :{0}, len {1}".format(s[i:i+match_length], match_length )
                    
                    return

        match_length = match_length - 1


    return -1







if __name__=="__main__":
    main()

