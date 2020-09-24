#!usr/local/bin
# write a program that takes an arithmetical expression in RPN
# and returns the number that expression evaluates to
import unittest


def RPN(s):
    s = s.split(",")

    operators = {
            "+":lambda x,y: x+y,
            "-":lambda x,y: x-y,
            "x":lambda x,y: x * y,
            "/":lambda x,y: x/y
            }

    s.reverse()

    #operand1
    o1 = int(s.pop())
    o2 = int(s.pop())
    total = 0

    while (len(s) > 0):
        item = s.pop()
        if item in operators.keys():
            total = operators[item](o1, o2)
            o1 = total
        else:
            # it is an integer
            o2 = int(item)

    return total



class testing(unittest.TestCase):

    def test_happy_case(self):
        self.assertEqual(RPN("3,4,+"), 7)
        self.assertEqual(RPN("3,4,+,2,-"), 5)
        self.assertEqual(RPN("3,4,+,2,x,1,+"), 15)

if __name__=="__main__":
    unittest.main().result



