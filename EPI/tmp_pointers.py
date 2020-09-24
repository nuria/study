#!usr/local/bin

class BTN:
    def __init__(self, value, left=None, right=None):
        self.value = value;
        self.left = left
        self.right = right
        self.next = None

    def __str__(self):
        return self.value

def set_pointers(node):
    # root is a special case
    # set pointer of left node


    if not node:
        return

    if node.left:
        node.left.next = node.right
        print "{0} points to {1}". format(node.left, node.right)

    if node.next and node.right:
        node.right.next = node.next.left
        print "{0} points to {1}".format(node.right, node.next.left)

    set_pointers(node.left)
    set_pointers(node.right)



if __name__ =="__main__":

    d = BTN('D')
    e = BTN('E')
    f= BTN('F')
    g = BTN('G')

    b = BTN('B', d, e)
    c = BTN('C', f, g)
    root = BTN('A',b,c)


    set_pointers(root)



