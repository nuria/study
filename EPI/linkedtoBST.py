#!/usr/local/bin

# convert a doubly linked list into a BST

class LItem():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return "<- {0}->".format(self.value)

# this defines a node for a bst
class Node():
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        selft.left = left

    def __repr__(self):
        "L:{2}<-{0}->R:{1}".format(self.value, self.right, self.left)


def _len_list(tail):
    #returns length of a linked list, it needs to traverse list to do so
    l = 1

    node = tail
    while (node.left is not None):
        node = node.left
        l +=1
    return l


def main():
    head =LItem(2)
    node3 = LItem(3, head)
    node5 = LItem(5,node3)
    node7= LItem(7, node5)
    node11 =LItem(11,node7)

    head.right = node3
    node3.right = node5
    node5.right = node7

    tail = node11

    def build_tree(tail):
        # L: linked list 
        # we can use recursion
        # TODO: we are calculating this over and over, optimize 
        l = _len_list(tail)

        print "len of list :{0}".format(l)

        if l == 1:
            return l

        if l == 2:
            left = tail.left
            left.left = None
            left.right =None
            return tail
        
        if l == 3:
            right = tail
            root = tail.left
            left =  root.left
            root.right = right
            root.left = left
            
            right.right = None
            right.left = None
            left.right= None
            left.left = None
            
            return root

        # l 4 or more:
        # divide problem
        m = l/2
        i = 1

        root = tail
        while(i <=m):
            root = tail.left
            i += 1
        
        right_node = root.right
        # cut right side of tree off
        if right_node is not None:
            right_node.left = None
        
        tail.right = None

        left_node = root.left
        # cut left tree off
        left_node.right = None

        print "root:{0}, left:{1}, right:{2}".format(root, left_node, right_node)
        
        root.right = build_tree(tail)
        root.left = build_tree(left_node)

        return root

        
        


    print str(head)

    tree = build_tree(tail)

    print str(tree)

if __name__=="__main__":
    main()
