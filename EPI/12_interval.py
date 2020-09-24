#!/usr/local/bin

# write  a program which takes as input a set of integers represented by an array
# and returns the largest subset of integers in the array having the property that if two integers are
# in the subset, then so are all integers between them
# input [3, -2, 7, 9, 8, 1,2,0, -1, 5, 8]
# the largest subset is [-2, -1, 0, 1,2,3] so it returns 6
import collections

def  largest_contiguous_interval(a):
    a = sorted(a)
    # now that is sorted identify the intervals
    result = []
    for i in range(0, len(a)-1):
        candidate = None
        for j in range(i+1, len(a)):
            if abs(a[j]-a[i]) == j - i:
                candidate = a[i:j+1]
            elif candidate is not None:
                result.append(candidate)
                break

    longest = result[0]
    for r in result:
        if len(r) > longest:
            longest = r

    return longest


def largest_continuous_interval_no_sorting(a):

    a_map = collections.Counter(a)

    # now look in map whether for each entry we have entries going forward
    result = []
    tmp = []

    for item in a:
        tmp.append(item)
        next_item = item + 1
        while a_map.get(next_item) is not None:
            tmp.append(next_item)
            next_item +=1
        if len(tmp) > len(result):
            result = tmp
        tmp = []


    return result



if __name__== "__main__":
    a = [3,-2,7,9,8,1,2,0,-1,5,8]

    print largest_contiguous_interval(a)
    print largest_continuous_interval_no_sorting(a)
