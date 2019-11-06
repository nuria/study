#/usr/local/bin
import sys

import heapdict
"""
The first line has two space-separated integers  and , the number of nodes and edges in the graph.

Each of the next  lines contains three space-separated integers ,  and , the end nodes of , and the edge's weight.
The last line has an integer , denoting the starting node.
"""



h = heapdict.heapdict()

def mst(N, start):
    # empty set of nodes "visited"
    X = set()
    T = {}
    # initialize X
    X.add(start)

    T[start] = []

    tmp_h = []

    while  X.difference(N)!= 0:
        # get smallest edge that includes a node we do not have in X
        # if heap is empty  break
        if len(h) == 0 :
            break
        (key,value) = h.popitem()
        (u,v) = (key[0], key[1])

        if (u in X  and v not in X) or (v in X and u not in X):
            if (u in X and v not in X):
                T[u].append((v, value))
                T[v] = []
                X.add(v)
            else:
                T[v].append((u, value))
                T[u] = []

                X.add(u)
            # restore heap
            for item in tmp_h:
                h[item[0]] = item[1]
            tmp_h = []
        else:
            tmp_h.append((key, value))
    # now add the weight of all edges in T
    cost = 0
    for k in T.keys():
        for item in T[k]:
            cost = item[1] + cost

    #print T
    return cost

def main():
    f = open(sys.argv[1])
    # first line is nodes and edges
    line = f.readline()
    (nodes, edges) = line.split()

    # all nodes
    N = set()
    G  = {}
    for l in range(int(edges)):
        items = f.readline().split()
        items = map(int, items)
        N.add(items[0])
        N.add(items[1])
        if G.get(items[0]) is None:
            G[items[0]] = []
        # do we need the graph?
        G[items[0]].append((items[1], items[2]))
        # we need the heap, it is a global variable
        h[(items[0],items[1])] = items[2]

    start = int(f.readline())
    #print G
    print mst(N, start)

if __name__=="__main__":
    main();
