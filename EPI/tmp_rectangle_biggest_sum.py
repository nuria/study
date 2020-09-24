#usr/local/bin

"""
Matrix: find rectangle at origin with biggest sum

"""
def find_sum(A):
    #A[i][j]
    # i = row, j is column

    # this feels like it benefits from a DP-style solution

    # rectange that
    #S[y][x]

    max_row = len(A)
    max_column =  len(A[0])

    # index 1 more

    S = [[0] * (max_column + 1)  for i in range(0, max_row  + 1)]

    # S now is a matrix with all zeroes


    for y in range(1, max_row +1 ):

        for x in range(1, max_column +1):

            S[y][x] = S[y-1][x] + S[y][x-1] + A[y-1][x-1]
            # do not double count
            S[y][x] -= S[y-1][x-1]

    return S



if __name__=="__main__":

    A = [[6,5,-9,2], [-2, -5, -2, -7], [3, -2,10, 13], [-8, 3, 1, -2]]

    S = find_sum(A)

    for i in A:
        print i

    for i in S:
        print i
