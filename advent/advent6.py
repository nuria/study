#!usr/local/bin
import sys

"""
AAA) BBB
direct orbit
B orbits A
"""

if __name__ == "__main__":
    f = open(sys.argv[1])
    G = {}

    U = []
    V= []

    # source vertexes
    edges = []
    for l in f:
        (u,v) = l.strip().split(")")
        # we are going to build a directed graph
        # COM)B
        # u, v
        # but first we need to find the source vertexes
        U.append(u)
        V.append(v)
        edges.append((u,v))

    # looks like there is only 1 sun
    sun = (set(U)-set(V)).pop()


    # now the edges
    # if we build the right graph (if we assume there are a few or one source vertexes)
    # it is a matter of just adding the weight of all edges

    G = {}
    for (u,v) in edges:
        #edge will be from sum to moon
        if G.get(u) is None:
            G[u] = []
        if G.get(v) is None:
            G[v] = []
        G[u].append(v)

    # will hold the path from G to all nodes, the sum of all those paths are the orbits
    # this assumes there is just 1 path
    # depth first search
    # lifo
    q = list()
    # python list pop() pos from the end
    D = {}
    # initialize all distances
    INFINITY= 1000000;
    for k in G.keys():
        D[k] = INFINITY


    D[sun] = 0

    explored = []
    explored.append(sun)

    q.append(sun)
    while (len(q)>0):
        node = q.pop()
        if len(G.get(node)) > 0:
            edges = G[node]
            for e in edges:
                if e not in explored:
                    D[e] = D[node] + 1
                    # we assume just one path to each node, super simplifying
                    explored.append(e)
                    q.append(e)

        else:
            explored.append(node)

    distance = 0

    for k in D:
        distance += D[k]

    print distance











