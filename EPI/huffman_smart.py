#!/usr/bin/python
import sys
import heapdict

"""
Our frequencies are  A=5, B=2, R=2,C=1 and D=1

encoding: 0 111 10 0 110 0011010111100

should read: ABRACADABRA
"""
import copy

class Node:
    def __init__(self, label, value, left= None, right=None):
        self.label = label
        self.value = value
        self.left = left
        self.right = right

    def pretty_print(self):
        s = self.label + " "
        s_left = ''
        s_right = ''
        if self.left:
             s_left = self.left.pretty_print()
        if self.right:
            s_right = self.right.pretty_print()

        return s + s_left + s_right

    def __str__(self):
        return self.label + " " + str(self.value)

# builds a huffman tree from the frequencies
def huffman(f):
    h = heapdict.heapdict()
    for k in f:
        node = Node(k[0], k[1])
        h[node] =k[1]

    while len(h) >1:
        # get two shortest items
        (node1,p1) = h.popitem()
        (node2,p2) = h.popitem()
        node3 = Node(node1.label + node2.label, node1.value + node2.value, node1, node2)
        h[node3] = node1.value + node2.value

    (tree, value)  = h.popitem()

    d = {}

    def build_dict(node, acu):
        if node.left:
            build_dict(node.left, acu +'0')
        if node.right:
            build_dict(node.right, acu + '1')

        if not node.left and not node.right:
            d[acu] = node.label


    build_dict(tree, '')

    return d


def decode(stream, d):
    message = ""

    # pointer for the stream
    i = 0

    substream =  ''

    while(i < len(stream)):
        substream  += stream[i]
        if d.get(substream) is not None:
            message = message + d[substream]
            substream = ''

        i = i + 1

    return message


if __name__=="__main__":
    f = [('A',5), ('R',2), ('B',2), ('D',1,), ('C',1)]
    d = huffman(f)
    print d
    stream = '01111001100011010111100'
    print decode(stream, d)

