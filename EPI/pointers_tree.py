#!/usr/local/bin

class node:
    def __init__(self, label,left=None, right=None):
        self.label = label
        self.right = right
        self.left = left
        self.next = None

def main():
    # initialize tree 
    D = node('D')
    E = node('E')
    F = node('F')
    G = node('G')
    C = node('C', F, G)
    B = node('B', D, E)
    root = node('A', B, C)

    # if you add all nodes to an array => [a,b.c,d,e,f,g]
    # every node just points to teh one next to it
    # given node  at position i  its right node is R = 2i+1 and  L = 2i+2
    A = []
    # traverse tree 
    
    # this is one of the preorders
    # R, R, L
    A.append(root)

    def traverse(node):
        nonlocal A
        if node.right:
            A.append(node.left)
            A.append(node.right)

            traverse(node.left)
            traverse(node.right)   

    traverse(root)
    
    for i in range(0, len(A)-1):
        n = A[i]
        n.next = A[i+1]

    print (list(map(lambda x:x.label,A)))


if __name__=="__main__":
    main()
