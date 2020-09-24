#!usr/local/bin/python


import collections

"""
See https://www.geeksforgeeks.org/prefix-postfix-conversion/
prefix = *, +, A,B,-,C,D,  -> operand op1 op2
postfix = A, B, +,C, D, -, *-> op1, op2 operand
"""


stack = collections.deque()

operator_set = ('+', '-', '*', '/')

def prefix_to_postfix(prefix):

    # read the prefix expression from right to left
    # if the symbol is an operand push it onto the stack
    # if the symbol is an operator then push two operands from teh stack

    # create operand 1, operand2, operator

    for c in reversed(prefix):

        if c not in operator_set:
            # push into stack
            stack.append(c)
        else:
            # operator
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + c)


    postfix = stack.pop()

    return postfix


if __name__== "__main__":

    prefix = ['*', '-', 'A', 'B', '-', 'C', 'D']
    infix = ['(','A', '+', 'B',')', '*', '(', 'C', '+', 'D', ')']
    postfix = ['A', 'B', '+', 'C', 'D', '-', '*']

    print prefix_to_postfix(prefix)



