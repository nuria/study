#usr/local/bin

def all_subsets(s):

    # binary way
    # using "bitmasks"

    import math

    result = []
    # we need to loop
    # until we reach zero
    # loop through all integers
    for bitarray in range(1 << len(s)):
        r = []
        while bitarray >0:
            # extract right most bit

            right_most_bit = bitarray & ~( bitarray -1)
            position = int(math.log(right_most_bit,2))
            r.append(s[position])
            bitarray = bitarray & (bitarray-1)

        result.append(r)
    return result



def all_subsets_better(s):
    if len(s) == 1:
        return [s]
    else:
        # union two sides
        result = []
        other_sets = all_subsets_better(s[1:])
        result.append([s[0]])
        for item in other_sets:
            result.append(item)
            result.append([s[0]]+ item)
        # a list of lists
        return result




if __name__=="__main__":

    r = all_subsets([1,2,3,4,5])
    print r
    print len(r)

    r2 = all_subsets_better([1,2,3,4,5])
    r2.append([])
    print r2
    print len(r2)
