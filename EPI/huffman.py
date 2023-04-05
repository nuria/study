#!/usr/bin

"""
Our frequencies are  A=5, B=2, R=2,C=1 and D=1

encoding: 0 1111001100011010111100

should read: ABRACADABRA

Note that given that frequencies coince and that huffman encoding is not 
deterministic it might read ARB..
"""
import heapq as h

class leaf():
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.leaf = True

    def __repr__(self):
        return " ({0}, {1})".format(self.value, self.freq)


class Node():
    def __init__(self, left, right, freq):
        self.right = right
        self.left = left 
        self.leaf = False
        self.freq =  freq

    def __repr__(self):
        return "intermediate, left: "+ str(self.left) + " right:" + str(self.right)


def main():
    f = []
    # a heapq and heap dict are not equivalent
    # a heapq returns (given two elements with identical priority) the one that was entered 1st?
    # a heapdict will return the one that was entered most recently

    h.heappush(f,(5,leaf('A',5)))
    h.heappush(f,(2,leaf('R',2)))
    h.heappush(f,(2,leaf('B',2)))
    h.heappush(f,(1,leaf('D',1)))
    h.heappush(f,(1,leaf('C',1)))
    
   
    print f

    def build_tree():
        
        # iterative solution? 
        # seems like recursion would do as well
        while len(f) > 1:
            (af,a) = h.heappop(f)
            (bf,b) = h.heappop(f)
            # these two are joined by an inside node
            # node :left , right
            i_node = Node(a,b, af+bf)
            h.heappush(f, (i_node.freq, i_node))

        
        print f[0]
        return f[0][1]

            
    
    def decode(text, tree):
        # rule is if 0 go left, if 1 go right
        msg =''
        i = 0
        current_node = tree

        while i  < len(text):

            if text[i] == "0":
                # go left 
                next_node = current_node.left  
                current_node = next_node
            else:
                next_node = current_node.right
                current_node = next_node
            print text[i] 
            print current_node

            if current_node.leaf:
                msg += current_node.value
                # go up and start over
                current_node = tree 
            
            i = i + 1
        
        return msg


    tree = build_tree()
    
    #txt = '0 1111 001100011010111100'
    txt = '01111001100011010111100'
    print decode(txt, tree)


if __name__=="__main__":
    main()
