#!/usr/local/bin
# play , 2 points (safety)
# 3 points (field goal)
# 7 points (touchdown)

# four combinations of plays yield a score of 12
# [2,2,2,2,2,2]
# [2,2,2, 3,3]
# [2,3,7]
# [4,4,4]


# write  aprogram that takes a final score for individual plays and returns the number
# of combinations of plays that result in the final score
# NOT the plays themselves but just the number of combinations


def plays(n, items):
    # in how many ways can you combine items to get n
    A = [[1] +[0] * 12  for j in range (0,3)]


    # mapping possibilities:
    #
    # 0 -> 0
    # 1 -> 2
    # 2 - >[2,3]
    # 3 - >[2,3,7]
    # A[i][j] -> i is choices and j is score

    # j is columns i is rows
    # A[1][2] =1
    print A

    W =[2, 3, 7 ]

    print A

    for i in range(0,2):
        for j in range(1,13):
            # candidate
            # 1 mapping possibility less
            if i > 1:
                without_this_play = A[i-1][j]
            else :
                without_this_play = 0

            with_this_play = 0
            n = 1
            while j-n * W[i] >= 0:
                with_this_play += A[i-1][j -n * W[i]]
                n += 1

            A[i+1][j] = without_this_play + with_this_play

    print A

if __name__=="__main__":
    plays(12, [2,3,4,7])



