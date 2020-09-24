#!usr/local/bin




class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def serialize_list(node):
    txt = ''
    while (node is not None):
        txt += " "+str(node.data)
        node = node.next
    return txt

def merge_two_sorted_lists(n1, n2):
    # we need two pointers
    p1 = n1
    p2 = n2

    dummy_head = None
    p = node(0)

    # nice trick
    dummy_head = p

    while p1 is not None and  p2 is not None:
        if p1.data < p2.data:
            p.next = p1
            p = p1
            p1 = p1.next
        else:
            p.next = p2
            p = p2
            p2 = p2.next


    # drain either list
    # nice trick
    p.next = p1 or p2
    return dummy_head.next


def sort_list(L):
    fast = L
    slow = L
    pre_slow = None

    if L is None or L.next is None:
        return L

    while fast and fast.next is not None:
        pre_slow = slow
        fast = fast.next.next
        slow =  slow.next


    if pre_slow:
        # this breaks list in two
        pre_slow.next  = None


    return merge_two_sorted_lists(sort_list(L), sort_list(slow))


if __name__=="__main__":
    _1 = node(1)
    _2 = node(2)
    _11 = node(11)
    _43 = node(43)
    _5 = node(5)
    _6= node(6)

    _6.next = _5
    _5.next = _43
    _43.next = _11
    _11.next = _2
    _2.next = _1

    print serialize_list(_6)
    print serialize_list(sort_list(_6))

    # list
    N1 = node(1)
    N3 = node(3)
    N5 = node(5)
    N1.next = N3
    N3.next = N5

    # list
    N4 = node(2)
    N5 = node(6)
    N6 = node(11)

    N4.next = N5
    N5.next = N6


    node = merge_two_sorted_lists(N1, N4)
    print serialize_list(node)
