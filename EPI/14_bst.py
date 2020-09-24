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


# return true if key is present
# complexity o(H) , height of tree
def search_bst(tree, key):
    if tree is None:
        return False

    if tree == key:
        return True
    elif key < tree:
        return search_bst(tree.right, key)
    else:
        return search_bst(tree.left, key)




def satisfies_bst_better(node):
    _minus_inf = float('-inf')
    _plus_inf = float('+inf')

    def are_keys_in_range(tree, low, high):
        if tree is None:
            return True
        else:
            if tree.data > low and tree.data < high:
                return  are_keys_in_range(tree.left, low, tree.data) and are_keys_in_range(tree.right, tree.data, high)


    return are_keys_in_range(node.left, _minus_inf, node.data) and are_keys_in_range(node.right, node.data, _plus_inf)


def satisfies_bst_better2(node):
    # let's try an inorder transversal that stores the last visited node
    # should always be smaller as in order transversals print tree in order
    def inorder(node, prior, acumulator):

        if node.left is not None:
            inorder(node.left, node.data, acumulator)
        # when we are here, what was the one prior
        acumulator.append(node.data)

        if node.right is not None:
            inorder(node.right, node.data, acumulator)

        return acumulator

    result = inorder(node, None, [])

    return result



def satisfies_bst_BFS(tree):

    # we keep tuples like (node, less_than, more_than)
    q = collections.deque()

    # we move on a bread first manner keeping on the queue
    # the items that met the constrain given by the parent node

    q.append((tree,float('-inf'), float('inf')))

    while len(q) > 0:
        # get item
        (node, _lower, _higher) = q.popleft()
        if node.data > _lower and node.data < _higher:
            # bst property maintained, continue
            if node.left:
                q.append((node.left, _lower, node.data))
            if node.right:
                q.append((node.right, node.data, _higher))
        else:
            return False

    return True


# o(n) in time and space, does not use BST prop
def first_key_greater_than(root, k):

    def inorder(root, result = []):
        if root.left:
            inorder(root.left, result)

        result.append(root)

        if root.right:
            inorder(root.right, result)

        return result

    result = inorder(root)

    print result

    for i in range(0, len(result)):
        if result[i].data > k:
            return result[i]

    return None


# let's try to use the bst property
def first_key_greater_than2(tree, k, candidate = None):
    if tree is None or tree.data == k :
        return candidate

    if k > tree.data:
        return first_key_greater_than2(tree.right, k, candidate )

    if k < tree.data:
        return first_key_greater_than2(tree.left, k, tree.data)

def largest_k_entries(tree, k):
    result = []

    def reverse_inorder(tree, k):
        if len(result) == k:
            return

        if tree.right :
            reverse_inorder(tree.right, k)

        if len(result) <k:
            result.append(tree)


        if tree.left:
            reverse_inorder(tree.left, k)


    reverse_inorder(tree, k)

    return result



if __name__=="__main__":

    node17 = BSTNode(17, BSTNode(13))
    node11 = BSTNode(11, None, node17)
    node3 = BSTNode(3, BSTNode(2), BSTNode(5))
    node7 = BSTNode(7, node3, BSTNode(11))

    node37 = BSTNode(37, BSTNode(29, None, BSTNode(31)), BSTNode(41))
    node23 = BSTNode(23, None, node37)
    node47 = BSTNode(47, None, BSTNode(53))

    node43 = BSTNode(43, node23, node47)

    root = BSTNode(19, node7, node43)

    print satisfies_bst_better(root)
    print satisfies_bst_better2(root)
    print satisfies_bst_BFS(root)

    print "first key"
    print first_key_greater_than(root, 13)
    print first_key_greater_than2(root, 13)

    print "largest keys"
    print largest_k_entries(root, 4)

