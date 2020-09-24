#!usr/local/bin

# think of ana array as a set of 1 dimensional sticks, length
# given by  int value
def water(A):
    # maximizing h * distance on array of both entries

    areas = {}
    max_area = (0,())

    for i in range(0, len(A)):
        item = A[i]
        # start looking at the end
        for j  in range(len(A)-1, i-2, -1):
            # entries do not have to be teh same
            # you just go with the shorter one

            area = min(item, A[j]) * (j-i)
            areas[(i, j)] = area
            if area > max_area[0]:
                max_area = (area, (i,j))

    return max_area

def water_1pass(A):
    # look at the beginning and end of array
    # go with higher stick on either side and check
    max_area = (0, ())

    i = 0
    j = len(A) -1
    while i < j:
        area = min(A[i], A[j]) * (j-i)
        if area > max_area[0]:
            max_area = (area, (i, j))
        # now if A[i] > A[j]
        # explore A[i] A[j-1]
        if A[i] >= A[j]:
            j = j-1
        else:
            i = i+1

    return max_area


if __name__=="__main__":

    print water([1,2,1,3,4,4,5,6,2,1,1,3,1,3, 2,1, 2,4,1])

    print water_1pass([1,2,1,3,4,4,5,6,2,1,1,3,1,3, 2,1, 2,4,1])


