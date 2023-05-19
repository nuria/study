#!/usr/local/bin

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __repr__(self):
        txt = "[" + str(self.value)+",("
        for n in self.neighbors:
            txt+= str(n.value) +","
        txt += ")" +"]"
        
        return txt

def main():
    # instantiate graph
    node0 = Node(0)
    node3 = Node(3)
    node2 = Node(2)
    node4 = Node(4)
    node1 = Node(1)

    node0.add_neighbor(node3)
    node0.add_neighbor(node2)
    node0.add_neighbor(node4)
    
    node3.add_neighbor(node2)
    
    node4.add_neighbor(node3)
    node4.add_neighbor(node1)
    
    node1.add_neighbor(node2)
    
    node2.add_neighbor(node0)

    # how to clone the graph effectively?
    # we get node0 and create it, follow all neighbors recursively?
    # kind of like a DFS
    visited = {}
    q = []
    q.append(node0)

    # pointer to new graph
    root = None

    print node0

    while len(q)> 0:
        node = q.pop()
        clone = Node(node.value)

        if root is None:
            root = clone

        visited[clone.value] = 1
        
        for n in node.neighbors:
            if visited.get(n.value) is None:
                q.append(n)
            clone.add_neighbor(n)
        
        

    print root

if __name__=="__main__":
    main()
