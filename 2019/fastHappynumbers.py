#!/usr/local/bin

import sys
import copy

# let's see if we can make this dynamic programmy
# acumulator is an acumulator of factors
# trying to avoid global state
results = []

def split(n, factors, acumulator):
    global results
    # let's make sure of basics
    smaller_factors = []
    for f in factors:
        if f <=n:
            smaller_factors.append(f)
    factors = smaller_factors

    # now if sum == n
    l = len(factors)
    if sum(factors) == n:
        return results.append(factors + acumulator)
    elif len(factors) > 1 and sum(factors) > n:
        # recurse
        for i in range(0, l):
            if (n-factors[i] >0):
                if i == 0:
                    before =  []
                    after = factors[1:l]
                elif i == (l-1):
                    after = []
                    before = factors[0:l-1]
                else:
                    after = factors[i+1:l]
                    before = factors[0:i]

                next_problem = split(n-factors[i], before + after, [factors[i]] + acumulator)
            elif (n-factors[i] == 0):
                results.append( [factors[i]] + acumulator)

    return results

def main():
    n = 6
    factors = [i for i in range(1,7)]
    split(n, factors, [])
    print results

if __name__== "__main__":
    main()
