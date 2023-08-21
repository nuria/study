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

    



if __name__=="__main__":

    main()
