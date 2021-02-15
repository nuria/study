#!/usr/local/bin
#Write pseudo code that take as input a natural number C ,
# and outputs all of the ways that a group of ascending positive numbers can
# be summed to give C . For example, if C = 6, the output should be
# 1+2+3
# 1+5
# 2+4
# 6
# and if C = 10, the output should be
# 1+2+3+4
# 1+2+7
# 1+3+6
# 1+4+5
# 1+9
# 2+3+5
# 2+8
# 3+7
# 4+6
# 10

import sys
import copy
solutions = []

# there is probably some dynamic programmming solution for this

def discloseSum(n, factors, acumulator=[]):
    global solutions
    smaller = []
    # loop through factors
    for f in factors:
        if  f <= n:
            smaller.append(f)

    if sum(smaller) == n:
        solutions.append(smaller + acumulator)
        return smaller + acumulator

    elif sum(smaller) > n:
        # check the case of removing one item at a time
        # thus making problem 1 item smaller

        for i in range(0, len(smaller)):
            if (n-smaller[i]) > 0:
                if i==0:
                    before = []
                else:
                    before = smaller[0:i]
                if i==len(smaller)-1:
                    after = []
                else:
                    after = smaller[i+1:len(smaller)]

                next_possible_solution =  discloseSum(n-smaller[i], before + after, acumulator + [smaller[i]])

            elif (n-smaller[i])== 0:
                solutions.append([smaller[i]]+ acumulator)
                return [smaller[i]] + acumulator

if __name__== "__main__":
    f = []
    n = int(sys.argv[1])

    for  i in range(1,n):
        f.append(i)

    discloseSum(n, f )

    print solutions


