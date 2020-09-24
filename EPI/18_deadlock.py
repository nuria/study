#/usr/local/bin
# for deadlock detection a "wait-for" graph is used
# in a wait for graph processes are represented as nodes
# and  an edge from P to Q implies Q is holding a resource that P needs
# thus P is waiting for Q

# so a cycle in this graph indicates a deadlock
# a cycle can be found by running BFS and seeing if a node we are visiting is alredy been visited
# the graph might not be connected so we need to run DFS from every vertex
import collections


class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self, label):
        self.label = label
        self.color = GraphVertex.WHITE
        self.edges = [] # list of GraphVertexes
    def __str__(self):
        return str(self.label)

# G is a list[GraphVertex]
def is_deadlocked(graph):
    # initially all vertexes are white, discovered , gray and finished (all subnodes are processed) black
    # if we "rediscover" a gray vertex (we come onto it again)
    # that is a cycle
    # since we have to do it for all nodes
    def has_cycle(vertex):
        # we should not be coming onto a node again
        #
        if vertex.color == GraphVertex.GRAY:
            return True
        else:
            vertex.color = GraphVertex.GRAY

        for v in vertex.edges:
            if v.color!= GraphVertex.BLACK:
                if has_cycle(v):
                    return True

        vertex.color = GraphVertex.BLACK

        return False


    for n in graph:
        if has_cycle(n):
            return True

    return False

if __name__=="__main__":

    # we use the representation of Node.edges = []
    # every node has a list of edges that point to other processes
    # let's build a test case

    n0 = GraphVertex(0)
    n1 = GraphVertex(1)
    n2 = GraphVertex(2)
    n3 = GraphVertex(3)

    n1.edges = [n2]
    n0.edges = [n1,n2]
    n3.edges =[]
    n2.edges = [ n0, n3]

    # what we pass to the function is a list of all nodes
    print is_deadlocked([n0,n1,n2,n3])


