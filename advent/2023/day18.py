#!/usr/local/bin

import sys

def main():

    f = open(sys.argv[1])

    # do we need the hex codes for anything?
    
    I = []
    
    RIGHT = 'R'
    DOWN = 'D'
    LEFT = 'L'
    UP ='U'


    (x0, y0, x1, y1) = (0,0,0,0)
    for l in f:
        l = l.strip()

        items  = l.split()
            
        d = items[0]
        u = int(items[1])

        I.append((d, u))


        if d =='R':
            x0 = x0 + u
        elif d =='L':
            x1 = x1 + u
        elif d == 'U':
            y0 = y0 + u
        else:
            y1 = y1 + u

    #print(I)

    

    EMPTY = '.'
    FULL ='#'


    G = []
    

    for i in range(0, y0+y1+1):
        G.append([])
        for j in range(0, x1+x0+1):
            G[i].append(EMPTY)
    

    def grid_representation(G):
        txt = ''
        for r in G:
            txt += "".join(list(r))
            txt += "\n" 
        return txt

    def capacity(G):  
        tally= 0 
        for i in range(0, len(G)):
            for j in range(0, len(G[0])):
                if G[i][j] == FULL:
                    tally = tally +1 
        return tally


    # now what 
    # we can paint borders easily but how do we
    # compute the inside areas
    # from reddit: shoelace formula


    # (U,6) U = direction, 6, units
    (i, j) = (y0,x1)
    
    print("x1: {0} x0:{1} ".format(x1,x0))
    print("y1: {0} y0:{1}".format(y1,y0))

    # Let's keep here the vectors that have been painted
    # somehow we are going to use those
    B = []

    for (d, units) in I:
        v = []
        
        if d == RIGHT:
            for k in range(j, j+units+1):
                G[i][k] = FULL
                v.append((i,k))
            j = j + units
        elif d == LEFT:
            for k in range(j, j-units-1, -1):
                G[i][k] = FULL
                v.append((i,k))
            j = j -units
        elif d == UP:
            for k in range(i, i-units-1, -1):
                G[k][j] = FULL
                v.append((k,j))
            i = i - units
        elif d == DOWN:
            for k in range(i, i+units+1):
                G[k][j] = FULL
                v.append((k,j))
            i = i +units
        
        B.append(v)
        
    print(grid_representation(G))

    print(capacity(G))
    
    # converte the lists to sets
    B = map (lambda x: set(x), B)
    B = list(B)

    #print( set.union(*V))
    # this is a better way to get the border size
    border = len(set.union(*B))

    print("border")
    print (border)


    print ('Vertexes')
    vertex = []
    for i  in range(0, len(B)-1):
        vertex.append(set.intersection(B[i],B[i+1]))

    vertex.append(set.intersection(B[-1], B[0]))



    # it is a list of sets [{(1,2)}, {(3,4)}]
    vertex = list( map(lambda x: list(x)[0], vertex))

    print(vertex)

    # to apply the shoelace formula the order in which these are listed is apparently important?
    # https://www.theoremoftheday.org/GeometryAndTrigonometry/Shoelace/TotDShoelace.pdf

    area = 0

    for i in range(0, len(vertex)-1):
        (y0, x0) = vertex[i]
        (y1, x1) = vertex[i+1]
        area += x0* y1 - x1*y0

    (y0, x0) = vertex[-1]
    (y1, x1) = vertex[0]
    area += x0*y1- x1*y0

    print(area/2)
    print((area+border)/2)






            




if __name__=="__main__":
    main()
