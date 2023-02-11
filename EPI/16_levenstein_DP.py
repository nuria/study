#!/usr/local/bin

import sys

def main():
    
    A = sys.argv[1]
    B = sys.argv[2]

    # a length A b length b
    D = [[0] * (len(B)+1) for i in range(0, len(A)+1)]


    # how does this matrix get initialized, ah maybe we need 1 row for 0,0
    # and the initial one for 0, 1 difference is one
    
    

    for a in range(0, len(A)+1):
        for b in range(0, len(B)+1):
            # are we always indexing at zero
            if a ==0:
                D[a][b] = b
            elif b == 0:
                D[a][b] = a

            elif A[a-1] == B[b-1]:
                D[a][b] = D[a-1][b-1]
            else:
                D[a][b] = 1 + min(D[a-1][b] , D[a][b-1], D[a-1][b-1])

    print D
    print D[len(A)][len(B)]



if __name__=="__main__":
    main()
