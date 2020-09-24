#!usr/local/bin/python
import unittest
from collections import deque

class node:
    def __init__(self, data):
        self.data = data
        self.prior = None

class EmptyQueue(Exception):
    pass

class Queue:
    # pointer to the head as it is FIFO
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prior = self.tail
            self.tail = node

    # return FIFO element
    def dequeue(self):
        if self.head == None:
            # that is empty queue
            raise EmptyQueue("data is empty")
        item = self.tail
        self.tail = self.tail.prior
        return item

class BinaryTreeNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self.data)


class testing(unittest.TestCase):
    def setUp(self):
        q = Queue()
        q.enqueue(node(5))
        q.enqueue(node(6))
        q.enqueue(node(7))
        q.enqueue(node(100))

        self.q = q

    def test_happy_case(self):
        self.assertEqual(self.q.dequeue().data, 100)

    def test_empty(self):
        q = Queue()
        with self.assertRaises(EmptyQueue):
            q.dequeue()



if __name__=="__main__":
    #unittest.main().result

    node28  = BinaryTreeNode(28)
    node0   = BinaryTreeNode(0)
    node271 = BinaryTreeNode(271, node28, node0)
    node17  = BinaryTreeNode(17)
    node3   = BinaryTreeNode(3, None, node17)
    node561 = BinaryTreeNode(561,node3)
    node6   = BinaryTreeNode(6,node271, node561)
    node28_r  = BinaryTreeNode(28)
    node271_r = BinaryTreeNode(271,node28_r)
    node641   = BinaryTreeNode(641)
    node401   = BinaryTreeNode(401,node641)
    node257   = BinaryTreeNode(257)
    node1     = BinaryTreeNode(1, node257, node401)
    node2     = BinaryTreeNode(2, node1)
    node6_r   = BinaryTreeNode(6, node271, node2)
    node314 = BinaryTreeNode(314, node6, node6_r)
    # now how do you print all nodes that are at the same level
    # using two queues
    q1 = deque()
    q2 = deque()

    a = []
    # the queue stores the levels but as we are shifting levels we move queus
    # the first node is known

    q = list()
    q.append(node314)

    while  len(q) >0:
        a.append([item.data for item in q])
        # now reenter all the  elememnts
        tmp = []
        for item in q:
            if item.right is not None:
                tmp.append(item.right)
            if item.left is not None:
                tmp.append(item.left)
        q = tmp

    for i in a:
        print i



