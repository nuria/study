#!/usr/local/bin

# convert a doubly linked list into a BST

class LItem():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        #"{1}<- {0}->{2}".format(self.value, self.left, self.right)
        
        #r = "{0}->{1}".format(self.value, self.right)
        l= "{1}<-{0}".format(self.value, self.left)
        return l

def _len_list(tail):
    #returns length of a linked list, it needs to traverse list to do so
    l = 1

    node = tail
    while (node.left is not None):
        node = node.left
        l +=1
    return l


def main():
    node2  = LItem(2)
    node3  = LItem(3)
    node5  = LItem(5)
    node7  = LItem(7)
    node11 = LItem(11)
    
    node2.right = node3
    node3.right = node5
    node5.right = node7
    node7.right = node11
    tail = node11
    head = node2
    

    node11.left = node7
    node7.left = node5
    node5.left = node3
    node3.left = head
   
    tail.right = None
    head.left = None


    def build_tree(tail):
        # L: linked list 
        # we can use recursion
        # TODO: we are calculating this over and over, optimize 
        l = _len_list(tail)

        if l == 1:
            return l

        if l == 2:
            head = tail.left
            head.left = None
            head.right =None
            print(tail)
            return tail
        
        if l == 3:
            root = tail.left
            head = root.left
            root.right = tail
            root.left = head
           
            head.left = None
            head.right = None
            tail.right = None
            tail.left = None
            print(root)            
            return root

        # l 4 or more:
        # divide problem
        m = l/2
        i = 0

        # find root
        # we really could find this when calculating list length
        root = tail
        while(i <=m):
            root = tail.left
            i += 1
        print "root node: {0}".format(root)


        right_node = root.right
        # cut right side of tree off
        if right_node is not None:
            right_node.left = None
        
        tail.right = None

        left_node = root.left
        # cut left tree off
        left_node.right = None

        print "root:{0}, left:{1}, right:{2}".format(root, left_node, right_node)
        
        root.right = build_tree(tail)
        root.left = build_tree(left_node)

        return root

        
    def print_tree(node):
        txt = ''
        print(node)
        if node.left is not None:
            txt += print_tree(node.left)

        txt += ' ' + str(node.value)
       

        if node.right is not None:
            txt += print_tree(node.right)

        return "[{0}]".format( txt)


    tree = build_tree(tail)
    print(tree)

    print print_tree(tree)

if __name__=="__main__":
    main()
