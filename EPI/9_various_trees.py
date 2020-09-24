#!usr/local/bin
import copy

class BinaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return "{" + str(self.data) + "R:"+ str(self.right) + "L:"+ str(self.left) +"}"


# With Parent
class BinaryTreeNodeWP(BinaryTreeNode):
    def __init__(self, data, left= None, right=None, parent= None):
        BinaryTreeNode.__init__(self,data, left, right)
        self.parent = parent



def is_balanced(root, balanced=True, height=0):
    if root is None:
        return (balanced, height)

    (balanced_l, h_l) = is_balanced(root.left, balanced, height+1)
    (balanced_r, h_r) = is_balanced(root.right, balanced, height +1)

    if h_l - h_r > 1 or balanced_r == False or balanced_l== False:
        return (False, 0)

    else:
        return (True, max(h_l, h_r) + 1 )



def is_symetric(r_tree, l_tree):
    if r_tree is None and l_tree is None:
        return True
    elif r_tree and l_tree:
        return r_tree.data == l_tree.data and is_symetric(r_tree.right, l_tree.left) and is_symetric(r_tree.left, l_tree.right)
    else:
        return False

path = {}

def find_lower_common_element(l1, l2):
    # starting from the end of both lists which is the element
    # that appears in both lists

    l1.reverse()
    l2.reverse()

    for  item in l1:
        # walk l2 until we find the fisyt match
        for k in l2:
            if item == k:
                return k



def lca(tree, node1, node2):

    """
    Can also use a named tuple
    @return (number_of_nodes, ancestor)
    """
    def lca_helper(tree, node1, node2):
        if tree is None:
            return (0, None)
        left_result = lca_helper(tree.left, node1, node2)

        if left_result[0] == 2:
            return left_result

        right_result = lca_helper(tree.right, node1, node2)

        if right_result[0] == 2:
            return right_result

        # now return for this tree
        # left + right plus this very node
        number_of_nodes =  left_result[0] + right_result[0] + (node1, node2).count(tree)

        # ancestor only makes sense if number_of_nodes == 2
        ancestor = None
        if number_of_nodes == 2:
            ancestor = tree.data

        return (number_of_nodes, ancestor)

    return lca_helper(tree, node1, node2)[1]


def inorder(tree, result = list()):
    if tree is not None:
        inorder(tree.left, result)
        result.append(tree.data)
        inorder(tree.right, result)

    return result


#root, left, right
def preorder(tree, result):
    if tree:
        result.append(tree.data)
        preorder(tree.left, result)
        preorder(tree.right, result)

    return result


def iterative_inorder(tree):
    prev, result = None, []

    # key is to record in 'prev' the root of the node fully visited
    # this only matters once we have traversed the right tree

    while tree:
        if prev is tree.parent:
            # keep going left
            # we have not explored this yet
            if tree.left:
                _next = tree.left
            else:
                result.append(tree.data)
                # done with left so go up
                _next = tree.right or tree.parent
        elif tree.left is prev:
            # we came to the tree from its left side
            # add parent
            result.append(tree.data)
            _next = tree.right or tree.parent
        else:
            # done with both children , move up
            _next = tree.parent

        prev, tree = tree, _next


    return result




if __name__=="__main__":

    #(self,data,left=None,right=None)
    node28  = BinaryTreeNode(28)
    node0   = BinaryTreeNode(0)
    node271 = BinaryTreeNode(271, node28, node0)
    node17  = BinaryTreeNode(17)
    node3   = BinaryTreeNode(3, node17)
    node561 = BinaryTreeNode(561, None, node3)
    node6   = BinaryTreeNode(6,node271, node561)
    node28_r  = BinaryTreeNode(28)
    node271_r = BinaryTreeNode(271, None, node28_r)
    node641   = BinaryTreeNode(641)
    node401   = BinaryTreeNode(401,None, node641)
    node257   = BinaryTreeNode(257)
    node1     = BinaryTreeNode(1, node401, node257)
    node2     = BinaryTreeNode(2, None, node1)
    node6_r   = BinaryTreeNode(6, node2, node271_r)
    node314 = BinaryTreeNode(314, node6, node6_r)

    print "is _balanced"
    print is_balanced(node314)

    _node3 = BinaryTreeNodeWP(3)
    _node3_s = BinaryTreeNodeWP(3)
    _node2 = BinaryTreeNodeWP(2, None, _node3)

    _node2_s = BinaryTreeNodeWP(2,_node3_s)
    _node6 = BinaryTreeNodeWP(6, None, _node2)
    _node6_s = BinaryTreeNodeWP(6,_node2_s)
    _node314 = BinaryTreeNodeWP(314, _node6, _node6_s)

    _node6_s.parent = _node314
    _node6.parent = _node314

    _node2.parent = _node6
    _node2_s.parent = _node6_s

    _node3.parent = _node2
    _node3_s.parent = _node2_s

    _node314.parent = None

    print is_symetric(_node314.right, _node314.left)

    # solution should be node 1
    print "least common ancestor"
    print lca(node314, node641, node257)


    print "inorder transversal"
    print inorder(node314, list())

    #print "inorder transversal, small"
    print inorder(_node314, list())

    print "iterative inorder"
    print iterative_inorder(_node314)
    print "preorder"
    print preorder(_node314, list())

