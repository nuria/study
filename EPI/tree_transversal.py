#!/usr/local/bin
# print all nodes on the tree that are at the same level

class Node:
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def is_leaf(self):
        return self.left is  None and self.right is None

    def __repr__(self):
        return str(self.value)

def main():
    
    def print_tree(node, acu):

        if node.left is not None:
            acu += "," + str(node.left)
        if node.right is not None:
            acu += ","+str(node.right)


        if node.left is not None:
            acu = print_tree(node.left, acu)
        if node.right is not None:
            acu = print_tree(node.right, acu)
        
        return acu

    node10 = Node(10)
    node26 = Node(26)
    node30 = Node(30)
    node80 = Node(80)
    node450 = Node(450)

    node25 = Node(25, node10, node26)
    node75 = Node(75, node30, node80)
    node350 = Node(350, None, node450)
    node50 = Node(50, node25, node75)
    node200 = Node(200,None, node350)
    root = Node(100, node50, node200)

    acu = str(root)
    print acu

    acu = print_tree(root, acu)
    
    print acu
    


if __name__=="__main__":
    main()
