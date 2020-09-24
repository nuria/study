#!/usr/local/bin
import collections



class  BSTNode():
    def __init__(self, data = None, left= None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return "{"  + str(self.data) +"}"

    def __repr__(self):
        return self.__str__()

nodes = []

def preorder(node):
    global nodes

    if not node:
        return

    if node.left:
        preorder(node.left)

    nodes.append(node.data)

    if node.right:
        preorder(node.right)


def satisfies_bst_prop(root):
    # one way is to traverse tree with  a preorder transversal, if outcome is sorted
    # then we can assume that property is satisfied?
    # a preorder prints left root right

    preorder(root)

    # global variable nodes should now be filled
    # is it in order?

    for i in range(1, len(nodes)):
        if nodes[i] < nodes[i-1]:
            return False

    return True



def lca_helper(root, node1, node2):

    if tree is None:
        return (0,0)
    left_result = lca_helper(root, node1, node2)

    if left_result== 2
        return (root, 2)

    right_result = lca_helper(root, node1, node2)

    if right_result == 2




def LCA(root, node1, node2):
    # compute lca if no parent field
    # hint: when is the root the lca?
    # when they are both in different trees
    # get path to node 1 from root
    # get path to node 2 from root
    # compare paths

    # is root the lca?

    found_left_node1 = lca_helper(root.left, node1)
    found_left_node2 = lca_helper(root.left, node2)

    if found_left_node1 and found_left_node2:
        # common ancestor is on the left tree
        return LCA(root.left, node1, node2)
    elif (found_left_node1 and not found_left_node2) or (found_left_node2 and not found_left_node1):
        # common ancestor is root
        return root.data
    else:
        # common ancestor is on right tree
        return LCA(root.right, node1, node2)


if __name__=="__main__":

    node17 = BSTNode(17, BSTNode(13))
    node11 = BSTNode(11, None, node17)
    node3 = BSTNode(3, BSTNode(2), BSTNode(5))
    node7 = BSTNode(7, node3, BSTNode(11))

    node37 = BSTNode(37, BSTNode(29, None, BSTNode(31)), BSTNode(41))
    node23 = BSTNode(23, None, node37)
    node47 = BSTNode(47, None, BSTNode(53))

    node43 = BSTNode(43, node23, node47)

    root = BSTNode(19, node43, node7)


    print satisfies_bst_prop(root)

    print LCA(root, node23, node47)

