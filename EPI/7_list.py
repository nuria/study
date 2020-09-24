#!usr/local/bin
import copy

class ListNode:
    def __init__(self, data = 0, next= None):
        self.data = data
        self.next = next

    def __str__(self):
        return "data:" + str(self.data)


def search_list(node, data):
    while node.next is not None:
        if node.data == data:
            return node
        else:
            node = node.next

def insert_after(node, new_node):
    tmp = node.next
    node.next = new_node
    new_node.next = tmp

# delete the node pass this one
def delete_node(node):
    node.next =  node.next.next

def merge_two_sorted_lists(node_l, node_p):
    l = node_l
    p = node_p
    # dummy pointer
    root = ListNode()
    node = root


    while (l is not None  and p is not None):
        if  l.data < p.data:
            node.next = l
            l = l.next
        else:
            node.next = p
            p = p.next
        node = node.next

    node.next = p or l

    return root.next

def print_list(node, s):
    if node is not None:
        s+= str(node)
        return print_list(node.next, s)
    else:
        return s

def reverse_list(node, _from, to):
    # split list three ways
    # head, l2, l3

    root = ListNode()

    root.next =  node

    i = 1

    for i in range (1, _from-1):
        node = node.next
    #
    head = node
    print "l1 ends here" + str(head)

    # node.next needs to be updated
    sublist_iter = head.next
    for i in range(to -_from):
        # the fist item needs to jump one position
        # towards end of list
        # and we do this from to end times
        tmp = sublist_iter.next
        sublist_iter.next = tmp.next
        tmp.next = head.next
        head.next = tmp

    print str(head.next)

    return root


if __name__== "__main__":

    l1 = ListNode(11)
    l2 = ListNode(7)
    l3 = ListNode(5)
    l4 = ListNode(3)
    l5 = ListNode(2)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    # now another list
    p1 = ListNode(3)
    p2 = ListNode(7)
    p3 = ListNode(10)

    p1.next = p2
    p2.next = p3

    root = merge_two_sorted_lists(l1, p1)

    s = print_list(root, '')
    print s

    root = reverse_list(l1,2,4)

    s = print_list(root, '')
    print s

