#!usr/local/bin

# stores levels
L = {}

class Node:
    def __init__(self, label, left = None, right =None, _next = None):
        self.label = label
        self.right = right
        self.left = left
        self.next = _next



def input_level(node, level = 0):
    global L

    if L.get(level) is None:
        L[level] = []
    L[level].append(node)

    if node.left is not None:
        input_level(node.left, level+1)

    if node.right is not None:
        input_level(node.right, level+1)

    # mmm.. does this gurantee order
    # tested it does


def initialize_pointers():
    for level in L.keys():

        if level == 0:
            L[level][0].next = l[level][0]

        else:
            items = L[level]
            for i  in  range( 0, len(items)-1):
                # are these items on the right order?
                items[i].next = items[i+1]

            items[len(items)-1].next = items[0]


# in order to be able to do this in O(n)
# we need to get it done while walking the tree
def preorder(node, 1st_node_level):

    #print node.label
    if node is None:
        return

    if node.left:
        node.left.next = node.right
        print(node.left.label)
        print "next {0}".format(node.left.next.label)
        preorder(node.left)
    if node.right:
        print(node.right.label)
        if node.next:
            node.right.next  = node.next.left
            print "next: {0}".format(node.right.next.label)

        preorder(node.right)









if __name__== "__main__":

    # giveen a tree where each node has a unitiliazed next pointer initialize pointers to be
    # a circular linked list for that level
    # root node points to itself
    #initialize_levels(root)
    #initialize_pointers()
    # two pass O(n) in time and O(n) in space
    # how to do this in O(1) space?

    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)

    root = Node(1, n2,n3)

    preorder(root)
