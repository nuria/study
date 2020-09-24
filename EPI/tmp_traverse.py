#!usr/local/bin

# N is the size of the matrix we are traversing
# for simplicity is square
def traverse(N):
    # for dynamic programing we need to create a matrix of
    # of N + 1 I think
    A = [[0]*N for i in range(0, N)]

    # what is the base case here
    # when i or j =0

    print A
    A[0][0] = 0
    for i in range(0,N):
        A[0][i] = 1
        A[i][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            A[i][j] = A[i-1][j] + A[i][j-1]


    print A
    return A[N-1][N-1]

if __name__=="__main__":

    N = 5
    traverse(N)
