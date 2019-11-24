#!/usr/local/bin/python
"""
Each row consists of the node tuples that are adjacent
to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating
that this row corresponds to the vertex labeled 6.
The next entry of this row "141,8200" indicates that
there is an edge between vertex 6 and vertex 141
that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent
to vertex 6 and the lengths of the corresponding edges.
17      26,1275 45,5114 142,8016        83,4615
"""
import sys
import heapdict

distance = {}
# nodes connected to this node  list of tuples ( node, edge_value)
nodes = {}
INFINITY =  10000

# calculate distance from this node to all the others
def dijistra(origin):

    queue = heapdict.heapdict()

    for n in nodes.keys():
        queue[n] = INFINITY

    queue[origin] = 0

    while len(queue) > 0:
        (current_node, s)  = queue.popitem()

        next_node = None

        # update distance to all nodes reachable
        # by this one
        for edge in nodes[current_node]:
            u = edge[0]
            weight = edge[1]
            d = distance[current_node] + weight
            if distance.get(u) is None or distance.get(u) > d:
                distance[u] = d
                if queue.get(u) is not None:
                    queue[u] = d

        # the next node to explore is the one with minimun distance value
        # poping from heap on next round will get us that node

if __name__=="__main__":
    f = open(sys.argv[1])

    for l in f:
        l = l.strip()
        # splitting on whitespace
        items = l.split()
        # undo  tupls
        main_node = int(items.pop(0))
        nodes[main_node] = []
        for i in items:
            (node, edge) = i.split(",")
            nodes[main_node].append((int(node), int(edge)))


##############################
    origin = 1
    # just choose one destination
    distance[origin] = 0

    #print nodes
    print "ORIGIN 1"
    dijistra(origin)

    for d in sorted(distance.keys()):
        print "To:{0}: {1}".format(d,distance[d])
