#!/usr/local/bin/python

import sys
import md5
'''
The input file lines are space separated like:
value weight

'''

# knapsack2 problem
W = 2000000;#knapsack size
n = 500 ;#total number of items

#W = 10


def r_knapsack(i,w,values, weights, K):
    _hash = md5.new()
    _hash.update(str(i) + " -" + str(w))
    key = _hash.digest()


    if K.get(key) is not None:
        return K[key]

    if i == 0 or w ==0:
        K[key] = 0
    else :
        # what was the prior value at this weight
        wi = weights[i]
        vi = values[i]
        prior = r_knapsack(i-1, w, values, weights, K)
        # next value
        if w-wi > 0:
            current = r_knapsack(i-1,w-wi, values, weights, K) + vi
            K[key] = max(prior, current)
        else:
            K[key] = prior

    return  K[key]



def knapsack(values, weights, W):

    K = [ [0 for w in  range(0, W)] for i in range(0,4)]


    for w in range(0, W):
        for i in range(0,4):
            K[i][w] = 0

    LAST  = 0
    for i in  range(1, len(values)):
        for w in range(0, W):
            if i < 3:
                prior = i-1
                current = i
                _next = i+1
            elif i % 3 == 0:
                prior = 2
                current =3
            elif i % 3 == 2:
                prior = 1
                current =2
            else:
                prior = 3
                current =1

            LAST = current
            # items of weight w excludes item Vi
            excluding_current=K[prior][w]
            if  w -weights[i] > 0:
                including_current = K[prior][w- weights[i]] + values[i]
                K[current][w] = max(excluding_current, including_current)
            else :
                K[current][w] = excluding_current

    return K[current][W-1]

def main():
    f = open(sys.argv[1])
    # adding zeros makes it more clear?
    values = [0]
    weights = [0]
    for l in f:
        (value, weight) = l.split()
        values.append(int(value))
        weights.append(int(weight))

    sorted(values)
    sorted(weights)

    # print knapsack(values, weights,W)
    D = {}
    print r_knapsack(n, W, values, weights, D)


if __name__=="__main__":
    main();
