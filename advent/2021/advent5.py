#!usr/local/bin
import sys

lines = list(open(sys.argv[1]))

lines_i = []


x_max =0 
y_max = 0


# print matrix concisely for debugging
def print_matrix(G):
    txt = ''
    for i in range(0, len(G[0])):
        for j in range(0, len(G[i])):
            if G[i][j] == 0:
                txt = txt + '.'
            else:
                txt =  txt + str(G[i][j])
        txt = txt +"\n"
    return txt


###### READ DATA ########

for l in lines:
    p1, separator, p2 = l.split()
    x1, y1 = p1.split(',')
    x2, y2  = p2.split(',')
    
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    points = []
    

    if x1 == x2 or y1 == y2:
        # we need max x max y to see dimensions of grid
        tmp_max = max(x1, x2)
    
        if tmp_max> x_max:
            x_max = tmp_max
    
        tmp_max = max(y1,y2)

        if tmp_max > y_max:
            y_max = tmp_max

        # calculate points in this line
        if x1 == x2:
            # only increment y
            delta = abs(y2-y1)
            # same point 
            if delta == 0:
                #lines_i.append([(x1, y1)])
                continue
            
            if y2 > y1:
                for i in range(y1, y2+1):
                    points.append((x1,i))
            elif y2 < y1:
                # y1 > y2
                for i in range(y2, y1 +1):
                    points.append((x1, i))

            lines_i.append(points)
            
        elif y1 == y2:
            # only increment x
            delta = abs(x2-x1)
            # same point 
            if delta == 0:
                #lines_i.append([(x1, y1)])
                continue
            
            if x2 > x1:
                for i in range(x1, x2+1):
                    points.append((i,y1))
            elif x2 < x1:
                # x1 > x2
                for i in range(x2, x1 +1):
                    points.append((i, y1))

            lines_i.append(points)
            
        

# this array now holds every point for every line as a element
#print lines_i

# GRID
row  = [0] * (x_max +1) 
G = []
for k in range(0, y_max+1):
    G.append(row[:])

print "x_max:{0}, y_max:{1}".format(x_max, y_max)


print print_matrix(G)

# now loop through array and build grid
overlap = 0 

for line in lines_i:
    for p in line:
        x = p[0]
        y = p[1]
        #print"{0}, {1}".format (x,y)
        G[y][x] = G[y][x] + 1


for i in range(0, len(G[0])):
    for j in range(0, len(G[i])):
        if G[i][j] >=2:
            overlap = overlap +1



print print_matrix(G)

print "overlap"
print overlap








