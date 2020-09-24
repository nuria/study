#/usr/lib/python

class BTN():

    def __init__(self, value, left=None, right= None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def lca_better(root, node1, node2):

    def find_parents(node, target1, target2):
        # keeps searching first left, right and root node
        # and adding to parents
        # returns tuple:(<0,1,2>, node)

        if node is None:
            return (0, None)
        else:
            # keep on searching
            # first left

            # no need to check if left is defined cause that is our case zero
            result_left  = find_parents(node.left, target1, target2)


            if result_left[0] == 2:
                return result_left

            result_right = find_parents(node.right, target1, target2)

            if result_right[0] == 2:
                return result_right

            result = result_left[0] + result_right[0]

            if result == 2:
                return (2, node)
            else:
                if node.value == target1.value  or node.value == target2.value:
                    return (result + 1, node)
                else:
                    return (result, None)

    (i, node) = find_parents(root, node1, node2)

    return node

def lca(root, node1, node2):

    def find_parents(node, target, parents=[]):
        # keeps searching first left, right and root node
        # and adding to parents
        # returns False if not found
        # returns True if found
        result = (False, [])

        if node.value == target.value:
            return (True, parents)
        elif node.left is None and node.right is None:
            return (False,[])
        else:
            # keep on searching
            # first left

            p = parents[:]
            p.append(node)

            if node.left is not None:
                result  = find_parents(node.left, target, p)

            if not result[0]:
                if node.right is not None:
                    result = find_parents(node.right, target, p)

        return  result

    (found, parents) = find_parents(root, node1)

    # we have now the parents of node1
    # one of them  has to be node2 parent
    # iterate on reverse order
    for p in reversed(parents):
        (found, other) = find_parents(p, node2)
        if found :
            return p
    return root



queue = []

def inorder(node):
    global queue
    if node.left is not None:
        inorder(node.left)
    queue.append(node)
    if node.right is not None:
        inorder(node.right)


if __name__ == "__main__":

    l_28 = BTN(28)
    l_0 = BTN(0)
    n_271 = BTN(271, l_28, l_0)

    l_17 = BTN(17)
    n_3 = BTN(3, l_17)
    n_561= BTN(561, None, n_3)

    n_6 = BTN(6, n_271, n_561)
    l_641 = BTN(641)
    l_28 = BTN(28)

    n_401 = BTN(401, None, l_641)
    l_257 = BTN(257)
    n_1 = BTN(1, n_401, l_257)
    n_2 =BTN(2, None, n_1)
    n_271 = BTN(271, None, l_28)
    n_6_r = BTN(6, n_2, n_271)

    root = BTN(314, n_6, n_6_r)

    inorder(root)

    print queue

    print lca(root, l_641, l_257)
    print lca_better(root, l_641, l_257)

