#!usr/local/bin/

# problem: write  aprogram that takes an array of strings and a set of strings and returns
# the indices of the starting and ending index of  a shortest subarray of the given array
# that covers the set
# [apple, banana, apple, apple, dog, cat, apple, dog, banana, apple, cat, dog]
# set [ banana, cat ]

# solution : {banana, apple, cat}

import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(a, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)

    remaining_to_cover = len(keywords)
    left = 0

    for right, p in enumerate(a):
        print "right :{0}, p :{1}".format(right, p)
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p]  >= 0:
                remaining_to_cover -= 1

    # keeps advancing until keywords to cover does not contain all keywords

        print "remaining to cover"
        print remaining_to_cover

        print "keywords to cover"
        print keywords_to_cover

        while remaining_to_cover == 0:
            print "result"
            print result
            if result == (-1, -1) or right-left < result[1] - result[0]:
                result = Subarray(left, right)

            print "left"
            print left
            p1 = a[left]
            if p1 in keywords:
                keywords_to_cover[p1] += 1
                if keywords_to_cover[p1]  >0:
                    remaining_to_cover +=1
            print keywords_to_cover
            left += 1

    return result






def is_set_covered(subarray, s):
    return all(elem in subarray for elem in s)

def is_set_covered2(subarray, s):
    # o(n)
    # convert subarray into hash/set and check if present
    return s in set(subarray)


def sortest_subarray(a, s):
    # start at index zero and move forward
    result = []

    for i in range(0, len(a)-len(s)):
        # start at index zero with the array that contains both sets
        # it needs to be at least the length of the set
        # do we do contains checks?
        for j in range(i+len(s) + 1, len(a)):
            if all(elem in a[i:j] for elem in s):
                result.append(a[i:j])
                break


    # now get minimun set
    subarray = result[0]
    for r in range(1, len(result)):
        if len(result[r]) < len(subarray):
            subarray = result[r]

    return subarray


if __name__=="__main__":
    a = ['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog']
    s = ['banana', 'cat']
    print sortest_subarray(a,s)
    print find_smallest_subarray_covering_set(a,s)
