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


# if binary tree represents a tree match the leafs
# can be participants

items = []
def participants(node):
    # do an inorder that only stores leafs?
    global items
    if node.left is None and node.right is None:
        items.append(node)
    else:
        if node.left:
            participants(node.left)
        if node.right:
            participants(node.right)



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
    r_28 = BTN(28)

    n_401 = BTN(401, None, l_641)
    l_257 = BTN(257)
    n_1 = BTN(1, n_401, l_257)
    n_2 =BTN(2, None, n_1)
    n_271_r = BTN(271, None, r_28)
    n_6_r = BTN(6, n_2, n_271_r)

    root = BTN(314, n_6, n_6_r)

    inorder(root)

    print queue

    participants(root)
    print items
