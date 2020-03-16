#!usr/local/bin



def knapsack(v,w,W):
    # for all zero weights and all zero values initialize to zero
    #
    A =[[0] * (W +1)  for i in range(0, len(v)) ]

    # confusing cause we have weights in columns and indexes representing values on rows

    for i in range(1, len(v)):
        for x in range(1, W + 1 ):

            without_item = A[i-1][x]

            if  x-w[i] > 0:
                with_item = A[i-1][x-w[i]] + v[i]
            else:
                with_item = 0

            A[i][x] = max(without_item, with_item )

    print A
    print A[-1][-1]

if __name__ == "__main__":

    W =10
    v = [0,10, 40, 30, 50]

    w = [0,5 , 4, 6, 3]

    knapsack(v,w, W)
