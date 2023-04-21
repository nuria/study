#/usr/local/bin

import sys


def main():
    l = eval(sys.argv[1])

    # if array is not sorted but it is sequential sum = n*(n-+1)/2
    # that would tell you what is missing 
    s = 0
    _min = float('inf')
    _max = 0
    
    for n in l:
        if n <_min:
            _min = n
        if n > _max:
            _max = n
        s += n
    _min = _min -1
    min_sum = _min*(_min+1)/2
    max_sum = _max* (_max+1)/2

    expected_sum = max_sum-min_sum

    print "The missing number:{0}".format(expected_sum-s)



if __name__=="__main__":
    main()

