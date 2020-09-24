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

"""
def longest(txt):
    subseq = {}

    longest = 0

    for i in range(0, len(txt)):
        for j in range(i + 1, len(txt)):
            if subseq.get(txt[i:j]) is None:
                subseq[txt[i:j]] =  []
            else:
                # entry already exists
                l = j - i
                if l > longest:
                    longest = l
            subseq[txt[i:j]].append((i, j))


    return longest


if __name__ == "__main__":

    print longest('AAAA')
    print longest('Oh toil toil toil trouble')



