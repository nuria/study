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


def main(I):
    label = 1
    ZERO = 0
    W = len(I[0])
    H = len(I)

    # index are (i,j) tuples
    visited = {}
    q = []

    # this does not visit all places exactly once
    # some are vsisted more than once

    for i in range(0, H):
        for j in range (0, W):
            
            if visited.get((i,j)) is None:
                if I[i][j]!= ZERO:
                    # figure out island
                    q.append((i,j))
                   
                    while len(q) > 0:
                        (_i, _j) = q.pop()
                        
                        print "poping :{0}, {1}".format(_i,_j)

                        visited[(_i,_j)] = 1
                        I[_i][_j] = label 

                        # look N, S, E , W
                        direct = [(_i+1, _j), (_i, _j+1), (_i-1,_j), (_i, _j-1)]

                        for (y,x) in direct:
                            if visited.get((y, x)) is None and y < H and y >=0 and x >= 0 and x <W and  I[y][x] != ZERO:
                                q.append((y,x))
                                            
                    label = label + 1
                else:
                    visited[(i,j)] = 1


    for i in range(0, H):
        print I[i]



if __name__=="__main__":
    

    I = [[0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0],[0,1,1,1,0,0,0,1,0],[0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0]]
    
    main(I)
