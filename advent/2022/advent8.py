#!/usr/bin

import sys
import functools

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

    visibility = []

    for x in range(1, x_l-1):
        for y in range(1, y_l-1):
            t = F[y][x]
            
            print "{0}, ({1},{2})". format(t, x,y)

            vis = []
            
            current_vis = 0
            # left
            for k in range(x-1, 0-1, -1):
                current_vis = current_vis + 1
                if F[y][k] >= t:
                    break

            vis.append(current_vis)
            
            current_vis = 0
            # right
            for k in range(x+1, x_l):
                current_vis = current_vis + 1
                if F[y][k] >= t:
                    break

            vis.append(current_vis)

            # up
            current_vis = 0
            for k in range(y-1,0-1, -1):
                current_vis = current_vis + 1
                if F[k][x] >=t:
                    break

            vis.append(current_vis)
            
            # down
            current_vis = 0
            for k in range(y+1,y_l):
                current_vis = current_vis + 1
                if F[k][x] >= t:
                    break
            
            vis.append(current_vis)
            
            print vis
            visibility. append(functools.reduce(lambda a,b:a*b,vis))
    
        print visibility

    print "max visibility"
    print max(visibility)

if __name__=="__main__":
    main()
