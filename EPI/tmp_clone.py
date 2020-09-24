#!usr/local/bin
import collections

def clone(node_value, edges):
    # how do you effectively clone the graph?
    # can't you run BFS or DFS from the node in question?
    G = []
    q = collections.deque()

    q.append((node_value, edges))

    # writing DFS, poping last element entered

    while(len(q)> 0):
        (node_value, edges) = q.popLeft()
        G[node_value] = edges

        # e is a pair of (node_value, edge)
        for e in edges:
            if G.get(e[0]) is None:
                q.append(e)


    return G



if __name__ =="__main__":

    # assumning a matrix representation for the graph
    # where
    # node = [e1,e2,e3]

    clone(node_value, edges)

