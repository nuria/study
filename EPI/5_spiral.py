#!usr/local/lib

def spiral(A):
    # also rotate to have columns
    C = map(list, zip(*A))

    sp = []

    offset = 0
    size = len(A)

    while offset <= len(A)-2:
        print offset
        print sp
        # does only 1 element remain?
        if len(sp) == (size *size) -1 :
            sp.append(A[offset][offset])
            break

        # n-1 first row
        for e in  A[offset ][offset:size-offset -1]:
            sp.append(e)

        # n-1 last column
        for e in C[size-offset-1][offset:size -offset -1]:
            sp.append(e)

        # n-1 last row, reversed
        last_row = list(reversed(A[size-offset-1]))
        for e in last_row[offset:size - 1]:
            sp.append(e)

        first_column = list(reversed(C[offset]))
        for e in first_column[offset:size - offset - 1]:
            sp.append(e)

        offset = offset +1

    return sp

if __name__=="__main__":
    R = [[1,2,3],[4,5,6],[7,8,9]]

    R = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # spiral order is [1, 2, 3, 6, 9, 8, 7, 4, 5]

    print spiral(R)





