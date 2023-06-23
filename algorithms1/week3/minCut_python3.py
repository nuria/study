#!/usr/local/bin
import sys
import random as r
import copy

# return type is an integer
def get_random_node(G):
    return r.randrange(len(G.keys())-1)

# return type is an integer
def get_random_edge(_list):
    if len(_list) == 1:
        return 0

    return r.randrange(len(_list)-1)


def main():

    f = open(sys.argv[1])
    # file format is edge v1 v2 v3

    G = {}

    for l in f:
        items = l.split()
        for e in items:
            if G.get(e) is None:
                G[e] = []

        for e in items[1:]:
            G[items[0]].append(e)


    print (G)

    # the mincut goal is to compute the graph with fewest crossing edges
    # a graph might have more than 1 min cut as a graph with n edges has n-1 cuts
    # how do identify edges at random?


    def min_cut(G):
        while len(G.keys()) > 2:
            node_index = get_random_node(G)
            node = list(G)[node_index]
            edge_index = get_random_edge(G[node])
            edge = G[node][edge_index]

            #print ("node: {0} and edge {1}".format(node, edge))

            # now merge
            # node and edge become the new larger node
            G[node+edge] =[]
            # remove loops 
            for e in G[node] + G[edge]:
                # O(n) lookup on list
                # TODO this can be improved on large lists using the edge list that already exist 
                if e!=node and e!=edge:
                    G[node+edge].append(e)

            
            del G[edge]
            del G[node]
            # now retrofit all apperances of node or edge with 'node+edge'
            for k in G.keys():
                edges = G[k]
                for i in range(0, len(edges)):
                    e = edges[i]
                    if e ==node or e == edge:
                        edges[i] = node+edge

            #print(G)
        
        return G

    # let's do as many try-outs as len of keys
    i = 0
    _min = float('inf')
    while i < len(G.keys()):
        MG = min_cut(copy.deepcopy(G))
        # this is just one try
        nodes = list(MG)
        crossing = len(MG[nodes[0]]) 
        _min = min(crossing, _min)

        print ("Crossing edges :{0}".format(crossing))
        
        i +=1 

    print ("min crossing edges: {0}".format(_min))

if __name__=="__main__":
    main()
