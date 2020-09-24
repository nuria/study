#!usr/local/bin/python

# team A behind team B
def photo( A, B)
    # if we sort both arrays
    A. sort()
    B.sort()

    # now if we want to put team A behind team B
    # every element of array A at position 'i'
    # has to be smaller than avery element of Array B at position i

    for i in range(0, len(A)):
        if A[i] >= B[i]:
            return False

    return True



if __name__=="__main__":
    # array of heights
    A = [1,3,4,7,9]
    B = [0,2,3,1,11]

