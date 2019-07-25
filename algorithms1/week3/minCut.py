#!/usr/binlocal/python
'''
#The file contains the adjacency list representation of a simple undirected graph.
#There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label,
#and the particular row (other entries except the first column) tells all the vertices
#that the vertex is adjacent to. So for example, the $$6^{th}$$ row looks like : "6	155	56	52	120	......".
#This just means that the vertex with label 6 is adjacent
#to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc


#Your task is to code up and run the randomized contraction algorithm for the min cut problem
#and use it on the above graph to compute the min cut.
#(HINT: Note that you'll have to figure out an implementation of edge contractions.
#Initially, you might want to do this naively, creating a new graph from the old every time
#there's an edge contraction.  But you should also think about more efficient implementations.)
#(WARNING: As per the video lectures, please make sure to run the algorithm many times
#with different random seeds, and remember the smallest cut that you ever find.)
#Write your numeric answer in the space provided.  So e.g., if your answer is 5, just type 5 in the space provided

Sample file:
    1 2 4
    2 1 3 4
    3 2 4
    4 1 2 3

'''
import sys
import random
import copy

# graph is going to be a hash:
# in which every entry is a vertex and the value is a list that represent the vertexes is linked to
# graph[1] = [2,3,4,5]

def buildGraphFromFile(_file):
    graph = {}
    f = open(_file)
    for l in f:
        items = map(int, l.split())
        vertex = items[0]
        edges = items[1:len(items)]
        graph[vertex] = edges
    return graph


def computeMinimunCut(graph):
    # if we only have two vertexes we are done
    if len(graph.keys()) <= 2:
        return graph

    # build list of edges to pick one at random
    E = []

    for k in graph.keys():
        for e in graph[k]:
            edge = (k,e)
            E.append(edge)

    t = random.choice(E)
    v = t[0]
    v_to_merge = t[1]
    edges1 = graph[v]

    # "collapse" to one vertex
    merged_vertex_name = v
    edges2 = graph[v_to_merge]

    # calculate union of the two edges lists
    # we are only contracting one edge at a time
    # this edge is (v,v_to_merge)
    final_edges = filter(lambda x: x!= v and x!=v_to_merge, list(edges1 + edges2 ))

    # delete original vertexes
    del graph[v]
    del graph[v_to_merge]

    # traverse graph, change references to v and v_to_merge with references to merged_vertex_name
    for k in graph.keys():
        tmp_edges  = []
        # rebuilding whole edges list
        for edge in graph[k]:
            if edge == v or edge == v_to_merge:
                tmp_edges.append(merged_vertex_name)
            else:
                tmp_edges.append(edge)
        # reset edges on current vertex to new list
        graph[k] = tmp_edges

    # enter new vertex
    graph[merged_vertex_name] = final_edges
    return computeMinimunCut(copy.deepcopy(graph))


graph = buildGraphFromFile(sys.argv[1])
#print graph

# start number of crossing edges to 2m, m being number of vertexes
num_vertexes = len(graph.keys())
crossing_edges = 2 * num_vertexes

i  =  20
minimun_cut = graph

while i > 0:
    _graph = copy.deepcopy(graph)
    local_minimum = computeMinimunCut(_graph)
    keys = local_minimum.keys();
    local_min_crossing_edges = len(local_minimum[keys[0]])
    # now count crossing edges
    if crossing_edges > local_min_crossing_edges:
        crossing_edges = local_min_crossing_edges
        minimun_cut = local_minimum
    i = i - 1


print ("crossing edges {0}"). format(crossing_edges)
print minimun_cut
