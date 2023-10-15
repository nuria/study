#!/usr/local/bin

# given a sorted cyclic list, insert value on list cyclic means the last element 
# points to the first or rather that there is no last no first 
# 1 -> 3 -> 5, value = 4

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "->" +str(self.value) + "->"


def main():
    _1 = Node(1)
    _2 = Node(2)
    _3 = Node(3)
    _4 = Node(4)
    _5 = Node(5)

    _3.left = _2
    _3.right = _5
    
    _5.left = _3
    
    _2.right = _3
    
    _1.right= _2
    _1.left = _5
    
    _5.right =_1

    def insert_node(node, list_node):
        # inserting node given another node on list 
        # we know list is sorted so we need to find min a move forward or max and move backwards
        # the 'end' of list is when node.next.value < node.value
        # and we rewind from that?

        current = list_node

        while (current.value < current.right.value):
            current = current.right
            print(current)


        # if condition is not satisfied we found the 'end'
        # end is largest number
        end = current 

        # edge  case
        # do we need to insert after end 
        if end.value < node.value:
            # undo "end"
            # item is bigger than last 
            first = end.right
            end.right = node
            node.left = end
            first .left = node
            node.right = first
        elif end.right.value > node.value:
            # item is smaller than first
            first = end.right
            end.right = node
            node.left = end
            node.right = first 
            first.left = node 

        else:
            # we need to insert in the middle 
            # do we need to loop the whole list?
            # there is no way to know
            # so starting with either end is fine
            current = end.right
            print(current)
            while (current.value < node.value):
                # advance
                current = current.right
                print(current)
            # found first element that is bigger
        
            previous = current.left
            current.left = node
            node.right = current
            node.left = previous

            previous.right = node

    linked_list = insert_node(_4, _1)

    # this is just for printing
    visited = []
    
    # print keeping track of what we have seen 
    
    node = _1
    while node.value not in visited:
        visited.append(node.value)
        print (visited)
        node = node.right


    print ("".join(map(lambda x: str(x), visited   )))




if __name__=="__main__":
    main()
