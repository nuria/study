#!usr/local/bin
import unittest
import random

# returns a size k subset of n where all subsets are equally likely
#o (n2)
def get_random_subset(n, k):
    r=[]
    for i in range(0, n):
        r.append(i)

    items_to_remove = n - k
    while (items_to_remove>= 0):
        next_item = random.randint(0, len(r)-1)
        r.pop(next_item)
        items_to_remove = items_to_remove -1

    return r

def get_random_subset_better(n,k):
    r=[]
    for i in range(0, n):
        r.append(i)

    # how close are we to having completed the set
    items_to_move = k

    while (items_to_move > 0):
        next_item = random.randint(k -items_to_move, len(r)-1)
        tmp = r[k-items_to_move]
        r[k-items_to_move] = r[next_item]
        items_to_move = items_to_move - 1

    return r[0:k]

if __name__=="__main__":

    print get_random_subset_better(10000000,45)
