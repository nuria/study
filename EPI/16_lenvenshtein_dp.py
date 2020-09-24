#!usr/local/bin



def lev(A,B):

    n = len(A)
    m = len(B)

    # makes n columns and m rows
    # access like L[m][n]
    L = [[0]* (n) for i in range(0, m +1)]


    # base case, we need to start from the front
    # if the other string is empty l distance
    # is the strings you have

    for j in range(1,m + 1):
        L[j][0] = j

    for i in range(1,n):
        L[0][i] = i



    for j in range(1, m +1):
        b = B[j-1]
        for i in range(1, n):
            a = A[i-1]

            if b == a:

                L[j][i] = L[j-1][i-1]

            else:

                L[j][i] = 1  + min(L[j][i-1], L[j-1][i], L[j-1][i-1])



    print L
    return L[m-1][n-1]




if __name__== "__main__":

    print lev("Carthorse","Orchestra")
