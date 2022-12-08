#!/usr/bin

import sys

import re as re

class node():
    def __init__(self,name):
        self.name = name 
        self.size = 0
        self.children = []
        self.parent = None
        self.files = []

    def set_size(self,size):
        self.size = size

    def add_file(self,file_size, file_name):
        self.size = self.size + file_size
        self.files.append((file_name, file_size))

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, node):
        self.children.append(node)

    def __repr___(self):
        print_tree(self)

# computing size per node recurses
def compute_size(node):
    if len(node.children)< 1:
        return node.size
    else:
        _size = node.size
        for c in node.children:
            _size =_size + compute_size(c) 

        return _size

def print_tree(node):
    if len(node.children) < 1:
        return "{ '"+ node.name+"': "+ str(node.size)+" , files:"+ str(node.files)+ "} "
    else:
        txt  =",{"+node.name+":"+str(node.size)  + ", files: "+ str(node.files)

        for c in node.children:
            txt = txt + print_tree(c)

        txt = txt + "}"
        
        return txt


def main():
    _input = sys.argv[1]
    f = open(_input)

    NODES = {}
    moves = []
    
    r_cd_up = re.compile('cd \.\.')
    r_cd = re.compile('cd \w.*')
    r_root = re.compile('cd /')

    for l in f: 
        l = l.strip()
        moves.append(l)

    root = node('/')
    current_node = root
   
    # do not assume all nodes are distinctly named
    NODES["/"] = root

    # we start at the root
    for m in moves[1:]:
        print m 
        if m.startswith('dir'):
            print "dir ..."
            # matches 
            # dir a
            (_dir, _name) = m.split(' ')
            child = node(_name)
            child.set_parent(current_node)
            current_node.add_child(child)
            NODES[current_node.name+"/"+_name] = child
        elif m[0].isdigit():
            # print m
            print "digits"
            # 2557 g
            # add to size of current dir
            (_bytes, name) = m.split(' ')
            current_node.add_file(int(_bytes), name)
        # $ command (but we have removed ls which are not useful)
        elif r_cd_up.search(m) is not None:
            # $ cd ..
            print "going up"
            current_node = current_node.parent
        elif r_cd.search(m) is not None:
            # $ cd a.
            print "moving into dir"
            (_shell, _cmd, _name) = m.split(' ')
            current_node = NODES.get(current_node.name+"/"+_name)

    
    
    
    # now each node has all files on it on its size but size for 
    # not leaf directories needs to be computed 
    total = 0
    print "We have {0} nodes".format(len(NODES.keys()))
        
    # dirs with size ad most 10,000
    for k in NODES.keys():
        n = NODES[k]
        #print "node" 
        #print n.name
        s = compute_size(n)
        #print s
        if s <= 100000:
            total = total + s

    print print_tree(root)
    print "total sum"
    print total 







if __name__=="__main__":
    main()
