#!/bin/python

"""
Calculate distance in an eually weighted graph

The first line contains an integer , the number of queries. Each of the following  sets of lines has the following format:

The first line contains two space-separated integers  and , the number of nodes and edges in the graph.
Each line  of the  subsequent lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , denoting the index of the starting node.

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.

Input:
2
4 2
1 2
1 3
1
3 1
2 3
2

Output:
6 6 -1
-1 6


"""


import sys
from collections import deque

# python fifo queue
# list.append() , adds at the end of the list
# list.popLeft(), removes the first item on list


# Complete the bfs function below.
# set of explored nodes
"""
    n = number-of-nodes
    m = number-of-edges
"""

def bfs(n, m, edges, s):
    # n = number of nodes
    # assume nodes are named sequentially
    # 1 to n
    # edge_case: is edges empty
    result = []
    explored = {}
    distance = {}
    # initialize s distance as zero
    distance[s] = 0


    EDGE_VALUE = 6
    Q = deque()
    Q.append(s)

    explored[s] = 1

    while len(Q) > 0:
        # fifo
        node = Q.popleft()

        # filter helps with perf, moves loop work to
        for edge in edges:
            next_node = None
            if node == edge[0]:
                next_node = edge[1]
            elif node == edge[1]:
                next_node = edge[0]

            if next_node is not None and explored.get(next_node) is None:
                distance[next_node] = distance[node] + EDGE_VALUE
                Q.append(next_node)
                explored[next_node] = 1


    # all distances should be in, for the nodes not there the distance is "-1"
    # result has to be reported in sequence
    for k in range(1, n+1):
        seen_root = False
        d = distance.get(k)
        if d is None:
            d = -1
        elif not seen_root and k == s:
            seen_root = True
            continue
        result.append(d)

    del edges
    return result

f = open(sys.argv[1])

q = int(f.readline())

for q_itr in xrange(q):
    nm = f.readline().split()
    (n,m) = map(int, nm)

    edges = []

    for _ in xrange(m):
        items = f.readline().rstrip().split()
        edges.append(map(int, items))

    s = int(f.readline())

    # edges looks like: [[1, 2], [1, 3]]

    # search start at s, know that if
    result = bfs(n, m, edges, s)

    print ' '.join(map(str, result))




