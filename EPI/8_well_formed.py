#!usr/local/bin/python
import unittest

# parsing problems benefit from a stack, LIFO property

def is_well_formed(s):
    s = list(s)
    # store the left parenthesis/bracket not mached
    stack = []


    # use the top of the stack as an indicator of the thing that needs to match next

    lookup = {")":"(", "]":"[","}":"{"}
    def matches_top(left, right):
        return lookup.get(right) == left

    def store(c):
        return c in lookup.keys()

    while (len(s) >0):
        c = s.pop()
        if store(c):
            stack.append(c)
        else:
            # see if there is a match
            # if stack is empty (meaning the companion
            # of "{,(,[" has not been seen been reading left to right
            # then
            # this is a fail
            if len(stack) == 0:
                return False
            else:
                item = stack.pop()
                if not matches_top(c, item):
                    return False

    # if there are items on stack at the end
    # something did not match
    print stack
    return len(stack) == 0



class testing(unittest.TestCase):

    def test_happy_case(self):
        self.assertTrue(is_well_formed("([]){()}"))
        self.assertFalse(is_well_formed("[()[]()()"))
        self.assertFalse(is_well_formed("[)]"))
        self.assertFalse(is_well_formed("[()[]{()()"))
        self.assertTrue(is_well_formed("(()[]){}"))

if __name__=="__main__":
    unittest.main().result
