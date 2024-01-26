#!usr/local/lib
import unittest
def list2graph(L):
    G = {}
    for item in L:
        G[item[0]] = item[1]
        for g in item[1]:
            if G.get(g) is None:
                G[g] =[]
        
    return G



def build_order(L):
    # we assume this is a graph
    # this is a topological sort
    # we need to have integers that we assign to nodes
    G = list2graph(L)

    
    # Using DFS

    # we return a structure that is a list of tuples
    # [(1,A), (2,B)]
    # would need to build A and B before building C
    q = []

    result = []

    # loop through all nodes and find one with only outgoing edges
    # from which we start DFS
    # that is teh last step
    candidates = {k:1 for k in list(G.keys())}
    
    for node in G.keys():
        for edge in G[node]:
            # mark with zero all nodes with incoming edges
            candidates[edge] = 0


    root = []
    for k in G.keys():
        if candidates[k] == 1:
            root.append(k)

    print (f'root node: {root}')
    # for now one node
    q.append((1,root[0]))
    order = 1
    visited = {}
    visited[root[0]] = 1

    print(G)

    while len(q) > 0:
        (order,n) = q[-1]
        print(q)

        children = G[n]
        print (f'{children}')
        all_visited = True
        for c in children:
            if visited.get(c) is None:
                q.append((order+1,c))
                visited[c] = 1
                all_visited= False


        if all_visited:
            result.append((order,n))
            q.pop()

    result.sort(reverse=True)
    return result



class TestSuite(unittest.TestCase):
    def test_happy_test(self):
        G = [("compile code", []),
        ("run linter", ["compile code"]),
        ("run unit tests", ["run linter"]),
        ("start test database", ["compile code"]),
        ("run integration tests", ["run linter", "start test database"]),
        ("deploy", ["run integration tests", "run unit tests"])]

        print (build_order(G))


if __name__=="__main__":
    unittest.main().result
