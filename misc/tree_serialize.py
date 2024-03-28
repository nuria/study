#!/usr/local/bin


class Node:
    def __init__(self, value ,  left=None, right=None):
        self.right = right
        self.left = left 
        self.value = value


output = []

def serialize(node):
    if node.left is not None:
        output.append(node.left.value)
    if node.right is not None:
        output.append(node.right.value)

    if node.left is not None: 
        serialize(node.left)
    else:
        output.append(None)

    if node.right is not None:
        serialize(node.right)
    else:
        output.append(None)


def deserialize(root, arr, curr_index =0):
    # Root, L, R
    # the left tree is at position 2n+1 
    # the right tree is at position 2n+2
    # if none is found stop traversing
    
    if arr[curr_index] is None:
        return
    
    left_index = 2*curr_index + 1
    
    if not  arr[left_index] is None:
        root.left = Node(arr[left_index])
        deserialize(root.left,arr, left_index)

    right_index = 2*curr_index + 2

    if not arr[right_index] is None:
        root.right = Node(arr[right_index])
        deserialize(root.right, arr,right_index)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3, node1, node2)

node5 = Node(5)
root = Node(4, node3, node5)

output.append(root.value)
serialize(root)
print(output)

_root = Node(output[0])
deserialize(_root, output)

output = []
output.append(_root.value)

serialize(_root)
print(output)

