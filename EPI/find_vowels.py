#/usr/local/bin
"""
Given a string s and an integer k, return the maximum number i
of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.i
"""

import unittest

VOWELS =('a','e','i','o','u')

def num_vowels(s, k):
    
    # abciiidef
    # We can compute the max num of vowels of string starting at i in 1 pass
    # cause we just need  to track 1 value, o(n)?
    
    # number of wovels of 1st window 
    v = 0

    for c in s[0:k]:
        if c in VOWELS:
            v +=1
    _max = v

    for i in range(1, len(s)-k+1):
        # how does values change, two fix lookups
        # top of window
        if s[i-1] in VOWELS:
            v = v -1
        if s[i+k-1] in VOWELS:
            v = v + 1 

        #print ("window:{0}, vowels:{1}".format(s[i:i+k],v))
        
        if _max < v:
            _max = v

    return _max



class testSuite(unittest.TestCase):

    def test_happy_case(self):
        n = num_vowels("abciiidef", 3)
        self.assertEquals(n,3)

        n = num_vowels("weallloveyou", 7)
        self.assertEquals(n,4)
        


if __name__=="__main__":
    unittest.main().result
