#!/usr/local/bin

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# input is a R, L, R transversal
import sys


class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
    
    def __repr__(self):
        txt = '{'
        txt +=  str(self.value)
        if self.left is not None:
            txt+= repr(self.left)
        if self.right is not None:
            txt+=repr(self.right)
        txt+= '}'

        return txt


def main():
    tree = eval(sys.argv[1]) #  [-10,9,20,None,None,15,7]
    # The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42

    nodes = []

    for i in range(0, len(tree)):
        if tree[i] !=  None:
            nodes.append(Node(tree[i]))
        else:
            nodes.append(None)

    l = len(nodes)

    for i in range(0, l):
        node = nodes[i]
        if node is not None:
            if 2*i + 1 < l:
                node.left = nodes[2*i+1]
                if node.left is not None:
                    node.left.parent = node
            
            if 2*i + 2 < l:
                node.right = nodes[2*i+2]
                if node.right is not None:
                    node.right.parent = node
    
    print nodes[0]
    
    # store partial sums
    # array of arrays?
    
    sums = []

    def find_sum(node):
        
        sum_left = 0
        sum_right = 0

        if node.left is None and node.right is None:
             return node.value
        
        if node.left is not None:
            sum_left = find_sum(node.left)
        
        if node.right is not None:
            sum_right = find_sum(node.right)
        

        _sum = max(sum_left , sum_right, sum_left + sum_right)  + node.value 
        sums.append(_sum)
        return _sum

    
    find_sum(nodes[0])

    print "max sum: {0}".format(max(sums))


if __name__=="__main__":
    main()
