#/usr/local/bin


import collections

class node():
    # label, value are just  to print them nicely
    def __init__(self, label, value=0,  left=None, right=None):
        self.right = right
        self.left = left
        # it is teh label what is unique
        self.label = label
        self.value = value    
    def __repr__(self):
        return "{0}, {1}".format(self.label, self.value)
        
    def set_right(self,node):
        self.right = node

    def set_left(self, node):
        self.left = node


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

# left -> root-> right
# o(n) time complexity
# o(h) space due to stack height
def inorder(node, path):
    if node.left is not None:
        inorder(node.left, path)
    path.append(node.label)

    if node.right is not None:
        inorder(node.right, path)

    return  path

# iterative inorder left->root->right
# o(n) time and o(h) space 
def i_inorder(node, path):
    visited = {}
    # LIFO
    q = []
    q.append(node)
    visited[node]=1 
    while len(q) > 0:
        node = q[-1]
        if node.left is not None and visited.get(node.left) is None:
            q.append(node.left)
            visited[node.left] = 1
        else:
            path.append(node.label)
            q.pop()
            if node.right is not None and visited.get(node.right) is None:
                visited[node.right] =1
                q.append(node.right)
    return path

# root-left-right
def preorder(node, path):
    
    path.append(node.label)
    if node.left is not None:
        preorder(node.left, path)
    if node.right is not None:
        preorder(node.right, path)

    return path

# builds tree with preorder and inorder transversals 
def build_tree(P,I):

   
    # we need to figure out what is left 
    # and what is right and recurse
    # P[0] is root
    
    if len(P) < 1:
        return

    root = P[0]
    root_node = node(root)

    print "preorder"
    print P
    print "inorder"
    print I
    
    print "root: {0}".format(root)


    if len(P) == 1:
        return root_node
    
    # now look for root in the inorder 
    i = 0
    while  I[i] != root:
        i = i + 1

    left_i = I[0:i+1]
    right_i = I[i+1:]

    left_p = P[1:len(left_i)]
    right_p = P[len(left_i):]

    
    left_tree = build_tree(left_p,left_i)

    right_tree = build_tree(right_p, right_i)

    root_node.set_right(right_tree)
    root_node.set_left(left_tree)

    return root_node



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

    print "postorder"
    print postorder(root, [])
    
    print "inorder" #left->root->right
    print inorder(root, [])
    print i_inorder(root, [])
    I =  inorder(root, [])
    
    print "preorder" # root ->left -> right
    print preorder(root, [])
    P = preorder(root, [])

    print ">>>>>"

    tree = build_tree(P, I) 
    # verify this is correct 
    print preorder(tree, [])


if __name__=="__main__":
    main()
