#usr/local/bin

"""
input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

"""

def deletion_distance(str1, str2):

    """
        0 d o g
      0 0
      f
      r
      o
      g
    """
     # could have a dp solution
    # D[r] rows
    # D[r][c] columns

    str1 = list(str1)
    str2 =  list(str2)

    l1 = len(str1) # rows

    l2 = len(str2) #columns

    D = [[0] * l2 for i in range(0, l1 + 1) ]

    # now set up lengths

    # D[r][c] => str1[0:r] abn str2[0:c]

    for c in range(0, len(D[0]) ):
        D[0][c] = c

    for r in range(0, len(D) ):
        D[r][0] = r


    for r in range(1, len(D)):
        for c in range(1, len(D[0])):
            if str1[r-1] != str2[c-1]:
                D[r][c] = min(D[r][c-1], D[r-1][c]) + 1
            else:
                D[r][c] = D[r-1][c-1]

    print D
    return D[-1][-1]




if __name__=="__main__":
    # should print 3 but prints 4
    print deletion_distance("dog", "frog")
