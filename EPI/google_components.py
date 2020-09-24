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


def label_connected(A):
    # columns, j
    n = len(A[0])
    # rows, i
    m = len(A)
    q = collections.deque()

    for i in range(0,m):
        for j in range(0, n):
            q.append((i,j))

    white = 0
    black = 1

    components = {}

    component_counter = 0

    visited = []

    while len(q)> 0:
        (i, j) = q.pop()
        if A[i][j] == white:
            # mark as visted and keep going
            visited.append((i,j))
        elif (i, j) not in visited:
            # need to do BFS from here to the rest of black nodes
            q_black = collections.deque()
            component_counter += 1
            components[component_counter] = []
            q_black. append((i,j))

            while len(q_black) > 0:

                (i,j) = q_black.pop()
                visited.append((i,j))
                components[component_counter].append((i,j))

                if i +1 < m and A[i+1][j] == black and (i +1 , j) not in visited:
                    q_black.append((i+1, j))

                if j+1 < n and A[i][j+1] == black and (i,j+1) not in visited:
                    q_black.append((i, j+1))

                if i-1 > 0 and  A[i-1][j] == black and (i-1, j) not in visited:
                    q_black.append((i-1, j))

                if j-1> 0 and A[i][j-1] == black and (i, j-1) not in visited:
                    q_black.append((i, j-1))

    # loop through all components on component counter

    for c in components.keys():
        l = components[c]
        for (i, j) in l:
            A[i][j] = c


    return A



if __name__=="__main__":

    G = [[0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0], [0,0,1,1,1,0,0,1,0],[0,0,1,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0]]


    print label_connected(G)







