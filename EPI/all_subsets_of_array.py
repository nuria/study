#!/usr/local/bin
# all subsets of array l, equivalent to thinking of a bittmap with as many positions 
# so [1,0,1] represents permutation [2,4]
# there are 2^N permutations where n i len of array
def main():
    l = [2,3,4]

    permutations = [[]]

    # number of permutations is 2^3
    for i in range(1,8):
        p = []
        index = 0
        while i > 0:
            if (i & 1) ^ 0 == 1:
                p.append(l[index])
            i = i >> 1
            index += 1
        permutations.append(p)

    print permutations


if __name__=="__main__":
    main()
