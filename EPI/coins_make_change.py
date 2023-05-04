#!/usr/localbin

def main():
    coins = [1,2,5]
    amount = 7

    # how many ways do we have to make 7 with these coins using them several times

    # this is really a tree of possibilities
    # start with one and proceed down the tree until possibilities find aount or exceed amount
    # this will find duplicates but 
    # there is also a DP solution?

    cache = {}

    # returns array of coins if it matchesi
    p = []

    def exact_change(cost, used):
        global possibilities 
        if cost in (1,2,5):
            for c in (1,2,5):
                if c == cost:
                    p.append(sorted(used + [c]))

        
        for j in (1,2,5):
            if cost-j > 0:
                exact_change(cost-j, used + [j])
            

        
    exact_change(7, [])
    for i in p:
        cache[str(i)] = 1

    print "all branches of the tree: {0}".format(len(p))

    print cache.keys()

    
    # this works but will include duplicated solutions
    def dp_change(coins, amount):
        # one dimensional cache
        # the way to think about it is that the way to make change for C amount is
        # D[C-coin[i]] + 1 if D[C-coin] exists  for all coins

        # we start at zero
        DP = [0] * (amount + 1 )
        
        print DP

        # for the smallest coin there is no change 
        for c in coins:
            DP[c] = 1

    
        for j in range(min(coins) + 1, amount+1):
            for c in coins:
                if j-c  > 0:
                    DP[j]+=DP[j-c]
                
                    
        print DP
        return DP[amount]

    print dp_change((1,2,5), amount)


if __name__=="__main__":
    main()
