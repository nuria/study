#!/usr/local/bin/python
#coding: utf-8
import unittest


class ListNode:

        def __init__(self, val, _next = None):
            self.val = val
            self.next = _next

        def __str__(self):
            txt = ''
            node = self

            while (node is not None):
                txt = txt +  str(node.val) + " -"
                node = node.next
            return txt


# recursive reverse, very scala


def reverse(node, head):
    if node is None:
        return (None, head)
    elif node.next is None:
        head = node
        return (node, head)
    else:
        rest = node.next

        (reversed_list_last_node, head) = reverse(rest, head)
        reversed_list_last_node.next = node
        node.next = None
    return (node, head)


class testing(unittest.TestCase):

    def setUp(self):
        node1 = ListNode(1)
        node2= ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5


        self.ll = node1

    def test_happy_case(self):
        (reversed_ll, head) = reverse(self.ll, self.ll)
        print head

        self.assertTrue(head.val == 5)

if __name__== "__main__":
    unittest.main().result

