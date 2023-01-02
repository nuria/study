#!/usr/bin

import sys
# from 42 to 24 and -314 to -413

# we can parse as a string and reverse but there is a more efficient solution

# You can represent the number in terms of powers of 10 in an array like
# [10, 100, 1000] or [1,1,1]
# do we start at teh highest or smallest power 
# make sense to start small and increase 

def main():

    _input = int(sys.argv[1])

    if abs(_input) < 10:
        print  _input
    sign = 1

    if _input < 0:
        sign = -1

    _input = abs(_input)

    # we store digits here
    tmp =[]
    _output = 0

    while _input !=0: # 413
        
        c = _input/10 #  413/10 = 41 / 41/10 = 4
        r = _input % 10 # 413 % 10 = 3  /41 % 10 = 1
        # integer division 
        # so
        _input = c # 41
        tmp.append(r) #[3]

        _output = (_output * 10) + r # 0*1 + 3 / 3 *10 + 1

    print _output * sign
        


if __name__ =="__main__":
    main()
