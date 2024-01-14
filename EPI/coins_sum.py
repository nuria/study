#!/usr/local/bin

"""
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. 
You want to know how many distinct sums you can make from non-empty groupings of these coins.

this can have a recursive or DP solution but this is a cool iterative answer

# https://stackoverflow.com/questions/43642133/complete-search-algorithm-for-combinations-of-coins

"""

def solution(coins,quantity):
    s = set([0])

    # do not iterate through combinations just sums
    for (i,c) in enumerate(coins):
        tmp = []
        for q in range(quantity[i]):
            tmp.append(c*(q+1))


        intermediate = []
        # now append all these to the set
        for item in s:
            for t in tmp:
                intermediate.append(t+item)


        s = set.union(s, intermediate)

    return len(s)-1

# should return 9
solution([10,50,100], [1,2,1])
