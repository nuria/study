#/usr/local/bin/python
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number 
of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
which this is possible, keep answer[i] == 0 instead.
"""
import sys
import unittest 

def main():
    # [73,74,75,71,69,72,76,73]
    data = eval(sys.argv[1])

    
    # let's first do the o(n2)
    answer = [0] * len(data)

    for i in range(0, len(data)):
        t = data[i]
        for j in range(i+1, len(data)):
            if data[j] > t :
                answer[i] = j-i
                break


    print (answer)

    # let's use a queue 
    # but rather than keeping values let's use the ideas of the monotonic stack
    # and keep indexes so we can "backtrack" and fill in pass values we have already pass

    answer2 = [0] * len(data)

    stack = []
    stack.append(0)

    for i  in range(1, len(data)):
        value = data[stack[-1]]
        while data[i] > value and len(stack) >0:
            _index = stack.pop()
            answer2[_index] = i -_index

        # current value is smaller than the ones we are keeping track in the stack
        stack.append(i)


    print (answer2)

if __name__=="__main__":

    main()
