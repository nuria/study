#!/usr/bin/python

# See page 363 of introduction to algorithms
# Rod cutting problem, given a rod of 'n' inches and a table of
# prices pi for i=1,2,3..
# Determine the maximum revenue rn obtainable by
# cuting the rod and selling the pieces
# note that if price pn for a rod of length n is large enough
# an optimal solution might require not cuting at all


prices = []
# price is per length i which happens to be the index of array
# so, say, price for length 2 meters is 5 dollars
prices = [0,1,5,8,9,10,17,17,20,24,30]

# using the idea that we cut a piece of length n
# in two pieces of length i and length n-i
# if we assume we further cut the piece of length
# n-i we really only have to recurse in one problem

cache = {}

sizes = {}
MINUS_INFINITY = -100
steps = {}


def cutRod(n):
    if cache.get(n) is not None:
       return cache[n]

    if n == 0:
        return 0

    q = MINUS_INFINITY
    for i in range(1, n +1):
        candidate = prices[i] + cutRod(n-i)
        if candidate > q:
            q = candidate
    cache[n] = q
    return  q


cache  = {}

for k in range(0,4):
    steps[k] = []

print cutRod(4)
print steps






