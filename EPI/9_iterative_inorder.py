#/usr/lib/python
import collections;


class BTN():

    def __init__(self, value, left=None, right= None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


queue = []

def _inorder(node):
    global queue
    if node.left is not None:
        _inorder(node.left)
    queue.append(node)
    if node.right is not None:
        _inorder(node.right)



def iterative_inorder(root):
    # lifo
    # pop from end
    parents = collections.deque()

    inorder = []

    node = root

    parents.append(root)

    while (node is not None):
        print inorder

        # traverse.left all the way
        if node.left is not None and node.left not in parents and node.left not in inorder:
            parents.append(node)
            node = node.left
        elif node.left is None and node.right is None:
            inorder.append(node)
            node = parents.pop()
        elif node.right is not None and node not in inorder:
            inorder.append(node)
            node = node.right
        elif node.left is not None and node.left in inorder:
            inorder.append(node)
            node = parents.pop()

    return inorder

def constant_inorder(node):
    prior = None
    inorder = []


    while (node is not None):
        print node
        print prior
        if prior == node.parent:
            # this is a right node
            if node.left:
                _next = node.left
            else:
                inorder.append(node)
                if node.right:
                    _next = node.right
                else:
                    _next = node.parent

        elif prior == node.left:
            inorder.append(node)
            if node.right:
                _next = node.right
            else:
                _next = node.parent
        else:
            _next  = node.parent


        prev = node
        node = _next

    return inorder



if __name__ == "__main__":

    l_28 = BTN(28)
    l_0 = BTN(0)
    n_271_l = BTN(271, l_28, l_0)
    l_0.parent = n_271_l
    l_28.parent = n_271_l



    l_17 = BTN(17)
    n_3 = BTN(3, l_17)
    l_17.parent = n_3



    n_561= BTN(561, None, n_3)
    n_3.parent = n_561


    n_6 = BTN(6, n_271_l, n_561)
    n_271_l.parent = n_6
    n_561.parent = n_6
    n_271_l.parent = n_6

    l_641 = BTN(641)
    l_28 = BTN(28)

    n_401 = BTN(401, None, l_641)
    l_641.parent = n_401

    l_257 = BTN(257)
    n_1 = BTN(1, n_401, l_257)
    n_401.parent = n_1
    l_257.parent = n_1

    n_2 =BTN(2, None, n_1)

    n_1.parent = n_2

    n_271 = BTN(271, None, l_28)
    l_28.parent = n_271

    n_6_r = BTN(6, n_2, n_271)
    n_2.parent = n_6_r
    n_271.parent = n_6_r

    root = BTN(314, n_6, n_6_r)

    _inorder(root)

    print queue
#    print iterative_inorder(root)
    print constant_inorder(root)

