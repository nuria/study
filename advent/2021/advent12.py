#!usr/local/bin
import sys
import copy 

lines = list(open(sys.argv[1]))

G  = {}

# G[node] = (edges)

for l in lines:
    l = l.strip()
    items = l.split('-')
    if G.get(items[0]) is None:
        G[items[0]] = []
    G[items[0]].append(items[1])
    # double edges
    #G[items[1]].append(items[0])

# {'A': ['c', 'b', 'end'], 'start': ['A', 'b'], 'b': ['d', 'end']}
print G

paths = []



# finds path to end node and appends entries to path
def find_path(node, visited, visited_d):
    if node == "end":
        paths.append(visited)
        return
    else:
        # keep on recursing
        if G.get(node) is not None:
            edges = G[node]

            for e in edges:
                # let's say is a directed graph
                if visited_d.get(e) is None:
                    visited_c = copy.copy(visited)
                    visited_c.append(e)
                    visited_d_c = visited_d.copy()
                    visited_d_c[e] = 1
                    find_path(e, visited_c, visited_d_c)
        else:
            # end node
            paths.append(visited)
            return

find_path('start', ['start'], {'start':1})


print paths
            

