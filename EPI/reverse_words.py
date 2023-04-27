#!/usr/bin
# reverse words in a sentence -> Hello world -> World Hello

import sys
import unittest


def main():
    # array of words
    def reverse(w):
        pass
        
        """
        Hello World
        
        
        treating string like a list of chars
        this once string is converted to a list is o(n) but no additional space

        """
        p1 = 0
        p2 = len(w) -1
        SPACE = ''
        # brute force solution
        words = w.split()
        for i in range(0, len(words)/2):
            print i
            top = words[i]
            end = words[len(words)-i-1]
            tmp = top
            words[i] = end
            words[len(words)-i-1] = tmp

        print words
            
            

    
    print  reverse('a b c d')
    print reverse ('Hello World')

class TestSuite(unittest.TestCase):
    def test_happy(self):
        pass

if __name__=="__main__":
    main()
    unittest.main().result
