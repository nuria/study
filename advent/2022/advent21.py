#!/usr/bin
import sys



OPS = {} 
MATH = set(['+', '-', '*', '/'])

def traverse(node):
    if not type( OPS[node]) == list :
        
        return OPS[node]
    else:
        rules = OPS[node]
        expr = ''
        for r in rules:
            if r in MATH:
                expr = expr + r
            elif r.isdigit():
                expr = expr + r

            else:
                expr = expr + traverse(r)
                
    return "("+expr+")"

def main():
    global OPS 
    f = open(sys.argv[1])


    for l in f:
        l = l.strip()
        (node, item) =l.split(':')
        if item.isdigit():
            OPS[node] = item
        else:
            OPS[node] = item.split()

    print OPS
    
    expr =  traverse('root')
    
    print expr 
    
    print eval(expr)


    # can we build a ginormous expression and eval it?
    # probably yes on example but not on real input

    





if __name__=="__main__":
    main()
