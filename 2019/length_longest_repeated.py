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

def computeRepetitions(s):

    # dictionary
    # A ->2
    # AB => 2
    # ABC =>2
    # ABCD =>0
    # ABCDE => 0

    # generate all possible substrings of string

    cache = []

    for i in range(0, len(s)):
        for j in range(i+1, len(s) + 1 ):
            cache.append(s[i:j])

    number_of_ocurrences = {}

    for c in cache:
        if number_of_ocurrences.get(c) is None:
            number_of_ocurrences[c] = 1
        else:
            number_of_ocurrences[c] = number_of_ocurrences[c] + 1

    # look for max length if repeated
    longest = 0
    chars = ''
    for k in number_of_ocurrences.keys():
        if  number_of_ocurrences[k] > 1 and len(k) >= len (chars):
            longest  = len(k)
            chars = k

    return (chars, longest)

if __name__ == "__main__":
    print computeRepetitions("AAAA")
    print computeRepetitions("Oh toil toil toil trouble")








