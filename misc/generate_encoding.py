#!/usr/local/bin

import unittest
# k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

import string
import collections

def decode(s):
    
    OPEN ="["
    CLOSE = "]"

    # this needs to return a string

    def unbundle(n, txt):
        result = ''
        for i in range(int(n)):
            result += txt
        return result
    
    def _decode(s):
        """
        2[a]
        push 2 push [ a
        when you come to ]
        unpush everything 
        aa
        2[b]
        works for linear case
    
        3[a2[c]]
        3, [, a
        if there is an int 
        push again
        2[c
        get to "]"

        c  2 stack has a 3
        unbundle
        push into stack
        cca
        until you get number
        pop
            
        """
        q = []
        
        n = ''
        txt = ''
        s = list(s)
        print(s)

        for i in range(len(s)):
            print (q)
            c = s[i]
            if c == OPEN:
                # push integer
                q.append(n)
                n = ''
            elif c.isnumeric():
                n += c
                if txt!='':
                    q.append(txt)
                    txt = ''
            elif c in string.ascii_letters:
                txt += c
            elif c == CLOSE:
                last = q.pop()
                if last.isnumeric():

                    # now we need to pop
                    decoded_text = unbundle(last, txt)
                    next_text = ''
                    if len(q) >0:
                        next_text = q.pop()
                    txt =  next_text + decoded_text 
                    q.append(txt)
                    txt = ''
                else:
                    # we have read it all
                    decoded_text = unbundle(q.pop(), last)
                    q.append(decoded_text)

        return q.pop()

    return _decode(s)

"""
3[a2[c]]

3 when [ push int q = [3]
a when int push q =[3,a]
2 when [ push int q = [3, a, 2]
c when close 
    timeto compute
    pop 2
    cc
    pop a
    acc
    q = [3,acc]
 c close
 pop 
    
"""


class TestCase(unittest.TestCase):
    def test_happy_case(self):
        self.assertEqual(decode("2[a]"), "aa")
        self.assertEqual(decode("2[a]3[b]"), "aabbb")
        self.assertEqual(decode("3[a2[c]]"), "accaccacc")



if __name__=="__main__":
    unittest.main().result

