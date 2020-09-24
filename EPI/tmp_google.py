#!usr/local/bin/python

"""
Given the following input array,
Input:0 0 0 0 0 0 0 0 0
      0 0 1 0 0 0 0 1 0
      0 0 1 1 1 0 0 1 0
      0 0 1 0 0 0 0 0 0
      0 0 0 0 1 0 0 0 0
Write a program that labels each of the connected components. For example, one output would be:
Output:0 0 0 0 0 0 0 0 0
       0 0 2 0 0 0 0 1 0
       0 0 2 2 2 0 0 1 0
       0 0 2 0 0 0 0 0 0
       0 0 0 0 3 0 0 0 0

"""

import collections

def label(G):
    #it is  a matrix that we can explore with i, j coordinates
    # but each element can be the element of  agraph

    C = len(G[0])

    R = len(G)

    ONE =1
    ZERO = 0

    def should_explore(x,y):
        if x>= 0 and y >=0  and x <= R-1 and y <= C-1  and A[x][y] == ZERO and G[x][y]==ONE:
            return True
        else:
            return False

    q = collections.deque()


    # G[row][colum]
    A = [ [0]* C for j in range(0,R)]


    label = 0


    for r in range(0, R):
        for c in range(0, C):
            if G[r][c] != ZERO and A[r][c]== ZERO:
                # found a component
                # now what
                # run DFS/BFS?
                q.append((r,c))
                label = label + 1
                while len(q) > 0:
                    (i, j) = q.popleft()
                    # label apropiately
                    A[i][j] = label
                    # go and look in 4 directions if not visited
                    if should_explore(i-1, j):
                        q.append((i-1, j))

                    if should_explore(i, j-1):
                        q.append((i, j-1))

                    if should_explore(i+1, j):
                        q.append((i+1, j))

                    if should_explore(i, j+1):
                        q.append((i, j + 1))

                  # keep going


    return A




if __name__=="__main__":
    G = [[0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0], [0,0,1,1,1,0,0,1,0],[0,0,1,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]
    print G
    print label(G)
