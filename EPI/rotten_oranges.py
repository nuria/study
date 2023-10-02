#!/usr/local/bin
"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

import sys
import collections


def main():
    
    # example: [[2,1,1],[1,1,0],[0,1,1]], output 4
    # that is in 4 steps all grid is rotten

    # let's use BFS and flip 1 to 2s the answer is the number of steps
    # FIFO

    q = collections.deque([]) # (row, column)

    B = eval(sys.argv[1])

    # the starting point (or there could be points) is an apple marked as '2'
    # mark adjacent as 2 as well and add them to the queue until no more apples are left


    ROTTEN = 2

    for i in range(0, len(B)):
        # square box
        for j in range(0, len(B[0])):
            if B[i][j] == ROTTEN:
                # last item is the fronteer step
                q.append((i,j, 0))

    # seems     
    steps = 0

    # no need to keeptrack of visited cause a ROTTEN is de-facto a visited
    while (len(q)>0):
        (i, j, f) = q.popleft()
        if steps < f:
            steps = f
        # find adjacents
        # North
        if i > 0 and B[i-1][j] != ROTTEN:
            B[i-1][j] = ROTTEN
            q.append((i-1, j, f +1))
        # south
        if i < len(B) -1 and B[i+1][j]!=ROTTEN:
            B[i+1][j] = ROTTEN
            q.append((i+1,j, f+1))
        # east
        if j >0 and B[i][j-1] != ROTTEN:
            B[i][j-1] = ROTTEN
            q.append((i, j-1, f+1))
        #west
        if j < len(B[i])-1 and B[i][j+1]!=ROTTEN:
            B[i][j+1] = ROTTEN
            q.append((i,j+1, f+1))

        

    # at this point the whole box is rotten
    # but we need to know the number of steps

    # this assumes all organges are rotten if they are not we would return -1
    # TODO

    print("Steps: {0}".format(steps))




if __name__=="__main__":
    main()
