#!usr/local/bin

import collections

# if max_row is 3 indexes are 0 t o3
def enclosed(D, max_row, max_column):
    # build a graph of whites (0) and another one of blacks(1)
    # if a  white graph does not have any boundary nodes
    # it is "enclosed"
    # now we will have many graphs

    # array of nodes
    G = []


    q = collections.deque()

    # get all whites on the boundary (whites are 0)

    for i in range(0, max_row + 1):
        for j in range(0, max_column + 1):
            if ((i == 0 or i == max_row) or (j == 0 or j == max_column)) and D[i][j]==0 :
                q.append((i,j))
                D[i][j] = 3

    print q

    while len(q) > 0:
        (i, j) = q.popleft()
        # get all reachable nodes
        if i  < max_row:
            if D[i +1][j] == 0:
                q.append((i+1, j))
                D[i+1][j] = 3
        if i > 0:
            if D[i-1][j] == 0:
                q.append((i-1,j))
                D[i-1][j] = 3
        if j < max_column:
            if D[i][j+1] == 0:
                q.append((i, j+1))
                D[i][j+1] = 3
        if  j > 0:
            if D[i][j-1] == 0:
                q.append((i, j-1))
                D[i][j-1] = 3

    return D



if __name__=="__main__":

    D = [[1, 1, 1, 1], [0,1,0,1],[1,0,0,1],[1,1,1,1]]

    print enclosed(D, 3, 3)

