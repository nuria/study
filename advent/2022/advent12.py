#!/usr/bin
import sys
import string
import heapdict



def find_node(G, S, E):
    q =  [] #heapdict.heapdict()
    visited = {}
    (i, j) = S
    
    found_E = False

    parents = {}
    
    parents[S] =  None
    
    visited[S] = True

    while True:
        height= G[i][j]
        if i == E[0] and j == E[1]:
            break
        
        # add children
        # up
        if i > 0 and visited.get((i-1,j)) is None and G[i-1][j] <= height +1 :
            q.append((i-1,j))
            parents[(i-1, j)] = (i,j)
            visited[(i-1,j)] = True

        # left 
        if j > 0 and  visited.get((i, j-1)) is None and G[i][j-1]<=height+1:
            q.append((i,j-1))
            parents[(i, j-1)] = (i, j)
            visited[(i, j-1)] = True

        # right
        if j < len(G[0])-1 and visited.get((i,j+1)) is None and G[i][j+1] <= height +1:
            q.append((i, j+1))
            parents[(i, j+1)] = (i, j)
            visited[(i, j+1)] = True

        # down
        if i <len(G) -1 and visited.get((i+1, j)) is None and G[i+1][j] <= height +1:
            q.append((i+1,j))
            parents[(i+1,j)] = (i,j)
            visited[(i+1, j)] = True

        
        print "({0},{1}) => {2} ".format(i,j, G[i][j])

        (i, j) = q.pop(0)
        
   
   # done with BFS
    path = 0
    node = parents[(i,j)]

    while node is not None:
        node  = parents[node]
        path = path + 1

    return path
        

def main():
    f = open(sys.argv[1])

    # H = ['a', 'b'
    # so H.index('a') gives height
    S = None
    E = None

    H = list(string.ascii_lowercase)
    
    def map_to_height(x):
        if x == "S" :
            return H.index('a')
        elif x == "E":
            return H.index('z')
        else:
            return H.index(x)

    G = []
    
    # map letters to numbers
    for l in f:
        tmp = list(l.strip())

        for i in range(0,len(tmp)):
            if tmp[i] == 'S':
                S = (len(G),i)
            if tmp[i] == 'E':
                E = (len(G), i)

        items  = map(lambda x : map_to_height(x), tmp)
        
        # need to build matrix
        G.append(items)

    # from S to E in as few steps as possible only using 1 jump 

    #print G
    print S # G[S[0]]S[1]
    print E # G[E[0]]E[1]

    print find_node(G, S, E)


if __name__=="__main__":
    main()
