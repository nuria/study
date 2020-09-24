#!usr/local/bin


# define each node with two pointers
class llNode:
    def __init__(self, value, _next = None, head = None):
        self.value = value
        # next node
        self.next = _next
        self.head = head

    def __str__(self):
        if self.value is None:
            return 'None ->'
        return self.value + "->"


def flatten(head):
    # simply walk the list
    node = head
    prior = None
    while (node is not None):
        if node.value is not None:
            # continue, lawful value
            prior = node
            node = node.next
        else:
            # this is the head of a list, two possible
            # ways, remove it (it is empty)
            # or flatten it
            if node.head is None:
                # remove this node, it is an empty head
                prior.next = node.next
                # prior does not change
                node = node.next
            else:
                # this node is the start of a list
                # find list end
                item = node.head
                while (item.next is not None):
                    item = item.next
                # item contains last node of this list
                prior.next = item
                item.next = node.next
                prior = item
                node = item.next

    return head


def print_list(head):
    node = head
    while (node is not None):
        print node
        node = node.next


if __name__=="__main__":
    # as coded all elements have null head pointers
    # not just one
    # the empty head that has to be removed just has '' value

    a = llNode('a')
    b = llNode('b')
    c = llNode('c')
    d = llNode('d')
    e = llNode('e')

    empty_1 = llNode(None)
    empty_2 = llNode(None)

    a.next = b
    b.next = empty_1
    empty_1.next = c
    c.next = empty_2

    empty_2.head = d
    d.next = e

    print_list(a)
    print "****"
    print_list(flatten(a))


