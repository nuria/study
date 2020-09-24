#!usr/local/bin


class BinaryTreeNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.data)



def is_balanced(root, balanced=True, height=0):
    if root is None:
        return (balanced, height)

    (balanced_l, h_l) = is_balanced(root.left, balanced, height+1)
    (balanced_r, h_r) = is_balanced(root.right, balanced, height +1)

    if h_l - h_r > 1 or balanced_r == False or balanced_l== False:
        return (False, 0)

    else:
        return (True, max(h_l, h_r) + 1 )








if __name__=="__main__":

    node28  = BinaryTreeNode(28)
    node0   = BinaryTreeNode(0)
    node271 = BinaryTreeNode(271, node28, node0)
    node17  = BinaryTreeNode(17)
    node3   = BinaryTreeNode(3, None, node17)
    node561 = BinaryTreeNode(561,node3)
    node6   = BinaryTreeNode(6,node271, node561)
    node28_r  = BinaryTreeNode(28)
    node271_r = BinaryTreeNode(271,node28_r)
    node641   = BinaryTreeNode(641)
    node401   = BinaryTreeNode(401,node641)
    node257   = BinaryTreeNode(257)
    node1     = BinaryTreeNode(1, node257, node401)
    node2     = BinaryTreeNode(2, node1)
    node6_r   = BinaryTreeNode(6, node271, node2)
    node314 = BinaryTreeNode(314, node6, node6_r)

    print "is _balanced"
    print is_balanced(node314)
