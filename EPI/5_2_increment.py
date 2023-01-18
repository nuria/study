#!usr/local/bin

import sys

import unittest


class TestSuite(unittest.TestCase):

    def test_happy_case(self):
        result = add([1,2,9])
        self.assertEqual(result, [1,3,0])


def add(_input):
    print "input"
    print _input
    # from [1, 2, 9] increment to [1,3,0]
    # brute force will be converting to integer and increment and to string again
    # but there is gotta be a better way
    
    # you can increment from the back and "carry over" to the front 

    #iterating the array in reverse
    carry = True
    
    for i in reversed(range(0, len(_input))):
        if carry:
            _input[i] = _input[i] + 1 # 9-> 10/ 2->3
            if _input[i] > 9: # 10 -> 9
                _input[i] = 0
                carry = True # true
            else:
                carry = False

    return _input

def main():
    _input = eval(sys.argv[1])
    print  add(_input)



if __name__=="__main__":
    # this interferes with test execution  uncomment to run
    #main() 
    unittest.main().result
