#!usr/local/python

class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return "{" + str(self.data) + "R:"+ str(self.right) + "L:"+ str(self.left) +"}"


def _rebuild(inorder, preorder):

    # base case
    if len(inorder) == 0:
        return None
    elif len(inorder) == 1:
        return Tree(inorder[0])
    else:
        # split
        parent = Tree(preorder[0])

        # this is o(n) on size of array
        # we can avoid this step by building a hash table and that would give us a o(1) index lookup
        index_of_root = inorder.index(preorder[0])
        left_inorder = inorder[0:index_of_root]
        right_inorder = inorder[index_of_root+1:]

        right_preorder = preorder[len(left_inorder) + 1: ]

        left_preorder = preorder[1:len(left_inorder) + 1]

        left_tree = _rebuild( left_inorder,left_preorder)
        right_tree = _rebuild(right_inorder, right_preorder)

        parent.right = right_tree
        parent.left = left_tree

    return parent


def inorder_walk(tree, result):
    if tree:
        inorder_walk(tree.left, result)
        result.append(tree.data)
        inorder_walk(tree.right, result)

    return result


def preorder_walk(tree, result):
    if tree:
        result.append(tree.data)
        preorder_walk(tree.left, result)
        preorder_walk(tree.right, result)

    return result


if __name__ == "__main__":

    # left, root, right
    inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
    # root, left, right
    preorder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']

    # from the preorder I know what is the root:
    tree = _rebuild(inorder, preorder)

    print "BLAH!"
    print inorder_walk(tree, list())
    print preorder_walk(tree, list())

