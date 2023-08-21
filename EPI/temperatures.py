#/usr/local/bin/python
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number 
of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
which this is possible, keep answer[i] == 0 instead.
"""
import sys

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
    # we can reverse an use a normal list
    data = reversed(data)

    answer2 = [0] * len(data)
    # queue where we temporaryly store looked up temps
    tmp = []
    
    i = 0
    while len(l) > 0:
        # get 1st element 
        t = data.pop()
           
        while (data[-1] < t):
            tmp.append(data.pop())

        data[i] = len(tmp)
        # now restore elements
        while(len(tmp) > 0):
            data.append(tmp.pop())


        i = i + 1 



if __name__=="__main__":

    main()
