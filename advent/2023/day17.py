#!/usr/local/bin

import sys
import collections
import heapq  as h

def main():

    f = open(sys.argv[1])

    G = []

    for l in f:
        row = list(l.strip())
        row_i = map(lambda x: int(x), row)

        G.append(list(row_i))

    # now the problem is finding min path with a few restrictions

    max_i = len(G) -1
    max_j = len(G[0]) -1
    

    print(G)

    q = []

    # we need to add every edge to graph with the
    # cost to reach plus its location
    
    MAX_STEPS = 3
    RIGHT = 'R'
    LEFT = 'L'
    DOWN = 'D'
    UP = 'U'


    # heat, (i,j, direction, steps)

    # TODO seems that we need here another initial condition
    h.heappush(q, (0, ( 0,0,'?',0)))
    

    visited = {}
    # keep (i,j, dir, steps) on visited
    

    # adapted dijistra

    while (len(q) > 0):
        (heat, (i, j, direction, steps)) = h.heappop(q)
        
        
        if visited.get((i,j, direction, steps)) is not None:
            continue
        
        visited[(i,j, direction,steps)] = heat

        # go right if you can and you were not going left
        if j < max_j and direction!=LEFT and   (not (direction==RIGHT and steps ==MAX_STEPS)):
            current_step = 1
            loss = heat + G[i][j+1]

            if (direction == RIGHT and steps < MAX_STEPS):
                current_step = steps + 1 

            if visited.get((i,j+1, RIGHT, current_step)) is None:
                h.heappush(q, (loss, (i, j+1, RIGHT, current_step)))

        if j > 0 and direction!= RIGHT and (not (direction==LEFT and steps ==MAX_STEPS)):
            current_step = 1
            loss = heat + G[i][j-1]

            if (direction == LEFT and steps < MAX_STEPS):
                current_step = steps + 1 

            if visited.get((i,j-1, LEFT, current_step)) is None:
                h.heappush(q, (loss, (i, j-1, LEFT, current_step)))

        # totally confused about reverse
        # if we are going right (down)
        # we cannot start to go left (up?)
        # down
        if i < max_i and direction!= UP and (not (direction==DOWN and steps ==MAX_STEPS)):
            loss = heat + G[i+1][j]
            current_step  = 1
            if direction == DOWN and steps < MAX_STEPS:
                current_step = steps + 1
            
            if visited.get((i+1,j, DOWN, current_step)) is None:
                h.heappush(q, (loss, (i+1, j, DOWN,current_step)))


        # UP
        if i > 0 and direction!= DOWN and (not (direction==UP and steps == MAX_STEPS)):
            current_step = 1
            loss = heat + G[i-1][j]
            if direction == UP and steps <MAX_STEPS:
                current_step = steps + 1
                
            if visited.get((i-1,j, UP, current_step)) is None:
                h.heappush(q,(loss , (i-1, j, UP, current_step)))

    

    # once we visisted the whole graph

    result = []
    # get all values for i = max_i and j = max_j 
    
    #print(visited)

    for k in visited.keys():
        (i, j, direction, steps) = k
        if i== max_i and j == max_j:
            result.append(visited[k])

    print (result)
    print(min(result))


if __name__=="__main__":
    main()
