#!usr/local/bin/python

import unittest
import heapq
# design an efficient method for sorting a k-increasing-decreasing array

def sort_k(a, k):
    # divide array in chuncks that are sorted
    # usea heap of size k to sort sorted arrays

    l = []
    j = 0
    while  j < len(a):
        l.append(a[j:j+k+1])
        tmp = a[j+k+1:j+2*k+1]
        tmp.reverse()
        l.append(tmp)
        j = j + 2* k + 1

    _heap = []

    result = []

    iterators = map(iter, l)

    for i in iterators:
        heapq.heappush(_heap, next(i))

    result.append(heapq.heappop(_heap))


    while (len(_heap) >0):

        for i in iterators:
            try:
                heapq.heappush(_heap, next(i))
                result.append(heapq.heappop(_heap))
            except StopIteration:
                # all iterators have same length
                if len(_heap) > 0:
                result.append(heapq.heappop(_heap))

    return result



if __name__=="__main__":
    a = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    print sort_k(a, 2)
