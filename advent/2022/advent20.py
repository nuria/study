#!/usr/bin

import sys
import collections
import copy

class Node():
    def __init__(self, value, left=None, right=None):
        self. value = value 
        self.right = right
        self.left = left 

    def __repr__(self):
        return "  " + str(self.left.value)+"<-"+str(self.value)+"->"+str(self.right.value)+" "


def swap_right(a):
    b = a.right
    swap(a, b)

def swap_left(a):
    b = a.left
    swap(b, a)

# a takes b position, moves right
def swap(a,b):
    
    a_left = a.left
    b_right = b.right

    #print "swaping: {0} by {1}". format(a,b)
    #print "Boundaries: {0}, {1}".format(a_left, b_right)

    a.right = b_right
    a.left = b
    b.right = a
    b.left = a_left
    
    b_right.left = a
    a_left.right = b

    #print b



def print_list(head, elements):
    node = head
    txt = ''
    
    for i in range(0, elements) :
        txt  = txt + str(node)
        node = node.right

    print txt
    


def main():
    f = open(sys.argv[1])
    message = []
    for l in f:
        l = l.strip()
        message.append(int(l))

    print message
    # now create circular list 
    tail = Node(message[-1])
    
    head = Node(message[0])
    head.left = tail
    tail.right = head

    NODES =[]
    NODES.append(head)
    
    INDEX_OF_ZERO = None

    current = head
    new_node = None
    for i in range(1, len(message)-1):
        new_node  = Node(message[i])
        current.right = new_node
        new_node.left = current
        current = new_node
        NODES.append(current)
        if current.value == 0:
            INDEX_OF_ZERO = i
                

    current.right = tail
    tail.left = current
    # set back pointer for tail
    tail.left = new_node
    NODES.append(tail)

    #print_list(head, len(NODES))
    

    # executed moves 
    current = None
    for i in range(0, len(message)):
        moves = message[i]
        # we find the node on the lookup
        current = NODES[i]
        #print "moving {0}".format(current.value)

        for m in range(0, abs(moves)):
            if moves > 0:
                swap_right(current)
            else:
                swap_left(current)
        #print_list(head, len(NODES))

    # now list is reshapped we need to find 
    # 1000th, 2000th, and 3000th
    CACHE = []

    # we will put the list on a cache
    current = NODES[INDEX_OF_ZERO]
    for i in range(0, len(NODES)):
        CACHE.append(current.value)
        current = current.right

    #print CACHE
    a = 1000 % len(NODES)
    print CACHE[a]

    b = 2000 % len(NODES)
    print CACHE[b]

    c = 3000 % len(NODES)
    print CACHE[c]

    print CACHE[a] + CACHE[b] + CACHE[c]

if __name__=="__main__":
    main()
