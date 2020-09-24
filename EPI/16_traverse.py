#!usr/local/bin


def traverse(n, m):

    A = [[0]*(m) for _ in range(n)  ]

    # A[i][j]

    # i = rows j columns
    # n=rows and m=columns

    for i in range(0, n):
        for j in range(0, m):

            if i == 0 :
                A[i][j] = 1
            if j == 0:
                A[i][j] = 1
            else:
                up = A[i-1][j]
                left = A[i][j-1]
                A[i][j] = up + left

    print A
    return A[-1][-1]

if __name__=="__main__":

    print traverse(5,5)

