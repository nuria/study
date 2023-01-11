#/usr/local/bin


import collections

class node():
    # label, value are just  to print them nicely
    def __init__(self, label, value,  left=None, right=None):
        self.right = right
        self.left = left
        # it is teh label what is unique
        self.label = label
        self.value = value    
    def __repr__(self):
        return "{0}, {1}".format(self.label, self.value)
        


def lca_helper(tree, n1, n2):
    # returns (int, node). int is 1 if node is present 2 if both
   
    if tree is None:
        return (0, None)
    
    (left_value, left_node) = lca_helper(tree.left, n1, n2)
   
    if left_value == 2:
        # found both nodes on left 
        return (left_value, left_node)
    
    (right_value, right_node) = lca_helper(tree.right, n1, n2)

    if right_value == 2:
        return (right_value, right_node)

    target_nodes = right_value + left_value + (n1.label, n2.label).count(tree.label)

    if target_nodes == 2:
        return(target_nodes, tree)
    else:
        return(target_nodes, None)


def postorder(node, path):
    
    if node is None:
        return path

    nodes = postorder(node.left, path) + postorder(node.right, path)
    
    nodes.append(node.label)
    
    return nodes




def main():
    m = node('M', 641)
    l = node('L', 401, None,m)
    n = node('N', 257)
    k = node('K', 1, l, n)
    p = node('P', 28)
    o = node('O', 271, None, p)
    j = node('J',2, None, k)
    i = node ('I', 6,j, o)
    d = node('D', 28)
    e = node('E', 0)
    h = node('H', 17)
    g = node('G', 3, h)
    c = node('C', 271, d, e)
    f = node('F', 561, None,g)
    b = node('B', 6, c, f)
    root = node('A', '314', b,i)

    (n, lca) = lca_helper(root, m, n)
    #print n 
    print lca

    print postorder(root, [])



if __name__=="__main__":
    main()
