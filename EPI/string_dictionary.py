#!/usr/lib

"""
You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary.
dictionary = ['apple', 'apple', 'pear', 'pie']
string ="applepie' =>Y
string =applepeer=>no
this is called word break on let code
"""
import sys

def main():
    # easy example: _input applepie, applepier
    d = set(['apple', 'apple', 'pear', 'pie'])
   
    # harder example: _input ='aaaaaaa'
    #d = set (['aaaa', 'aaa'])

    _input = sys.argv[1]

    # this is a tree , the 1st posibility that matches might not be the best 
    # so you have to keep on trying possibilities until an optimal combination

    _min = float('inf')
    _max = 0
    
    for w in d:
        if len(w) > _max:
            _max = len(w)
        if len(w) < _min:
            _min = len(w)

    # returns 1 if parseable according to dictionary, 0 otherwise
    # adding cache, this smells like DP
    # 1 if string is parseable, 0 otherwise
    # needs a cache to perform, which hints a DP solution

    def parseable(c,d, _max, _min):

        if len(c) > 0 and len(c) < _min:
            return 0
        if len(c) == 0:
            return 1

        j = 1
        i = 0

        possibilities = []
        while j <= len(c):
            s=c[i:j]
            if j <= _max:
                if s in d:
                    possibilities.append(parseable(c[j:],d, _max,_min))
                    print possibilities
                # also continue
                j = j + 1
            else:
                break

        if sum(possibilities) > 0:
            return 1
        else:
            return 0

    is_parseable = parseable(_input, d, _max, _min)

    if is_parseable > 0:
        print "True"
        return True
    else:
        print "false"
        return False


if __name__=="__main__":
    main()


