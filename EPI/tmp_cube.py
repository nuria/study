#!usr/local/bin

# given an equation a^3 + b^3 = c^3 + d^3
# find solutions in integers 1..1000
#




def solve_better(n):
    # precompute on cache cache[(a,b)] = a^3+ b^3
    cache = {}
    result = []

    # o (n *n) time
    # o (distinct operation) in space
    for a in range(1, n):
        for b in range(1,n):

            if a ==b:
                # avoid obvious
                next

            operation = a **3 + b **3

            # just add to cache results that matter


            if cache.get(operation) is None:
                cache[operation] = list()
            cache[operation].append((a,b))


    # now loop again trying to find the targets
    # o(n* n) in time

    for a in range(1,n):
        for b in range(1,n):
            target = (a **3 + b**3)


            if cache.get(target) is not None:
                for item in cache[target]:
                    if item[0]!=a and item[0]!=b:
                        l = sorted([a,b, item[0], item[1]])
                        # o (results) penalty
                        # can be mitigated with a hashmap that caches results with o(results) space penalty
                        if l not in result:
                            result.append(l)

    return result



if __name__=="__main__":
    print solve_better(100)
