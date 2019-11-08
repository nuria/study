#!/usr/bin/python
import sys
import heapdict

"""
Our frequencies are  A=5, B=2, R=2,C=1 and D=1

encoding: 01111001100011010111100

should read: ABRACADABRA
"""

decoder = {}

def printTree(node, txt):
    txt = txt + " ({0} , {1})". format(node.letter, node.prob)

    if node.leaf:
        return txt
    if node.left is not None:
        txt =  printTree(node.left, " < left "+ txt)
    if node.right is not None:
        txt = printTree(node.right, ">right"+ txt)
    return txt

class Node():
    def __init__(self, prob, letter, leaf= False):
        self.prob = prob
        self.letter = letter
        # marks empty nodes
        self.leaf = leaf
        self.right = None
        self.left = None

    def setRight(self, node):
        self.right = node


    def setLeft(self, node):
        self.left = node


def build_huffman(h):

    while len(h) > 1:
        (n1, f1) = h.popitem()
        (n2, f2) = h.popitem()
        root = Node(n1.prob + n2.prob, '0')

        root.setRight(n2)
        root.setLeft(n1)

        h[root] = root.prob

    # only one element in the heap
    # we are returning  a node but this is really a tree
    (root, value) = h.popitem()
    return root


def buildDecoder(node, values):
    # not super easy, do we loop char by char?
    # seems easier to figure out the "digits" per each letter
    # traversing the tree and decode using a dictionary

    if node.leaf:
        code = "".join(map(str,values))
        decoder[code] = node.letter
    else:
        if node.right is not None:
            buildDecoder(node.right, values+[1])
        if node.left is not None:
            buildDecoder(node.left, values+[0])



def decode(msg):
    d_msg = ''
    i = 0
    while i < len(msg):
        # one char fixes need to be handled separately
        if msg[i] in decoder.keys():
            d_msg = d_msg + decoder[msg[i]]
            i = i + 1
        else:
            for j in range(i+1, len(msg)):
                if msg[i:j] in decoder.keys():
                    d_msg = d_msg + decoder[msg[i:j]]
                    i =  j
                    break
    return d_msg


if __name__== "__main__":
    # frequencies of letters as an array of tuples
    freq = [('A',5),('B',2), ('R',2), ('C',1), ('D',1)]


    h = heapdict.heapdict()
    # we enter the chars on the heap on the order they appear
    # on the incoming string to break ties (?), this is the guideline from hacker rank problem
    for f in reversed(freq):
        n = Node(f[1], f[0], True)
        h[n] = n.prob

    root = build_huffman(h)

    print printTree(root, '')

    buildDecoder(root, [])
    print decoder
    print decode("01111001100011010111100")




