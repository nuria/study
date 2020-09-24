#!usr/local/bin



# graph made of vertexes  that have (<int> , list<vertexes>)
# list<vertexes> is a lif of refences
# design an algorithm that takes a reference to a vertex u and creates a copy to the graph
# on the vertexes reachable from u

import collections

class GraphVertex():
    def __init__(self,label, l = []):
        self.label = label
        # list of graph vertexes
        self.edges = l

def clone(u):

    # return the copy of u
    to_return = u.label
    G = {}

    d = deque()

    # star graph from here
    for v in u.edges:
        d.append(v)

    # can we use graph search to build the new graph?
    # G points from original to the copys
    G[u] = GraphVertex(u.label)


    while len(d) >0:

        vertex = d.popLeft()
        # now add edges reachable from that node
        for v in vertex.edges:
            G[vertex.label].edges.append(v)
            if v.label not in G.keys():
                G[v.label]  GraphVertex(v.label)
                d.append(v)

    return G[u.label]


    # given that this is a directed graph, would we have gottent to u, not if all are outgoing edges




if __name__=="__main__":


