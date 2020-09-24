#!usr/local/bin

def maze(G, start, end ):
    # let's assume G has the white pixes as enodes and pixes that are connected have
    # an edge, it is an undirected graph
    acumulator = []

    def DFS(start,end):
        # the recursive way
        acumulator.append(start)
        if G[start] is not None:
            # DFS
            if G[start][0] == end:
                accumulator.append(end)
            else:
                DFS(G[start][0], end)




    DFS(start, end)
    return acumulator

# node has color property or we have a color array/hashmap

def paint(G, point, M):

    d = collections.deque()

    d.append(point)
    color = M[point]
    reachable = []
    while len(d) >0:
        node = d.popleft()
        for p in G[node]:
            if p.color == color:
                d.append(p)
                # flip color
                # binary flip
                M[p.x][p.y]= M[p.x][p.y]








if __name__=="__main__":
    maze(G)
