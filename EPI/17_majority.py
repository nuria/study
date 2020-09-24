#!usr/local/bin


# identify objects in a sequence that occur more
# than a specified fraction of the total number of elements in the sequence

# you have a sequence of strings, you know that 'a priory'
# more than half the strings are repetitions but the positions of those elemts is unknown
# in 1 pass identify majority element
# with O(n) space easy, how do you do it without any additional space?
# you can also reduce the storage needed by randomizing the sampling to o(n/2)
# but that is a minor improvement, so, mmm, what else

def majority(A):
    # we can divide entries into two groups
    # we assign a majority entry and when its count decreases to zero we get another entry
    # hard to see that this guarantees the best solution
    candidate = A[0]
    count = 0

    for a in A[1:]:
        if a == candidate:
            count +=1
        elif a !=candidate and count == 0:
            candidate = a
            count = 1
        elif a !=candidate:
            count -= count



    return candidate


if __name__=="__main__":

    print majority(['b','a','c','a','a','b','a','a','c','a'])
