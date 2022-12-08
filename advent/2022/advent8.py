#!/usr/bin

import sys


def main():
    _file = open(sys.argv[1])

    # forrest
    F = []
    for l in _file:
        l = l.strip()
        F.append(map(lambda x: int(x), list(l)))

    print F
    y_l = len(F)
    x_l = len(F[0])

    print "number of trees on the outside" 
    outside = 2* x_l +2 *(y_l-2)
    print outside 

    # find islands, where all the way up to the edge a tree is shorter 
    # per every one position
    visible_trees = 0
    for x in range(1, x_l-1):
        for y in range(1, y_l-1):
            t = F[y][x]
            
            print "{0}, ({1},{2})". format(t, x,y)

            # if a tree is visible in one direction, it counts as visisble
            visible = True 
            for k in range(0, x):
                if F[y][k] >= t :
                    visible= False
                    break
            if visible:
                visible_trees = visible_trees +1 
                print "{0} is visible on 0,x".format(t)
                continue

            visible = True
            for k in range(x+1, x_l):
                if F[y][k] >= t :
                    visible= False
                    break
            if visible:
                print "{0} is visible on x+1".format(t)
                visible_trees = visible_trees +1 
                continue

            visible = True
            for k in range(0,y):
                if F[k][x] >= t :
                    visible= False
                    break
            if visible:
                print "{0} is visible on 0,y".format(t)
                visible_trees = visible_trees +1 
                continue

            visible = True
            for k in range(y+1,y_l):
                if F[k][x] >= t :
                    visible= False
                    break
            if visible:
                print "{0} is visible on y+1".format(t)
                visible_trees = visible_trees +1 
                continue
        
    print "visible trees"
    print outside + visible_trees


if __name__=="__main__":
    main()
