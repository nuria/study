#!/usr/local/bin
"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Add two linked lists as a number

"""
import sys

def main():
    # start right and carry over to the left 
    # you can do that with two pointers
    # but probably there is a better alternative?
    p1 = 0
    p2 = 0
    
    l1 = eval(sys.argv[1])
    l2 = eval(sys.argv[2])

    # we can carry over on the 2nd list 
    result = []
   
    len_1 = len(l1)
    len_2 = len(l2)

    l = max(len_1, len_2)

    i = 0
    carry = 0

    while i < l :
        p1 = i 
        p2 = i 
        if p1 <len_1:
            digit1 = l1[p1]
        else:
            digit1 = 0

        if p2 < len_2:
            digit2 = l2[p2]
        else:
            digit2 = 0
        
        _sum = digit1 + digit2 + carry
        
        carry = 0
        # [2,4,3] and [5,6,4]
        # first : 7, second: 10
        if _sum >= 10:   
            while _sum >= 10:
                carry += 1
                _sum = _sum -10 

        i = i + 1
        
        result.append(_sum)
            
    # we might need an extra digit
    if carry > 0:
        result.append(carry)

    print result

if __name__ =="__main__":
    main()

