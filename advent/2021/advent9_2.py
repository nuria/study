#!usr/local/bin
import sys




lines = open(sys.argv[1])

G = []

for l in lines:
    l = l.strip()
    if l is not None:
        item = map(lambda x : int(x),list(l))
        if item != '':
            G.append(item)

print G

lower = []

max_i = len(G)
max_j = len(G[0])


for i in range(0, max_i):
        low = True
        for j in range(0, max_j):
            # check all sides
            if j + 1 < max_j:
                if G[i][j] >= G[i][j+1]:
                    low = False
                    continue
            if i+ 1 < max_i:
                if G[i][j] >= G[i+1][j]:
                    low = False
                    continue
            if j - 1 >= 0:
                if G[i][j] >= G[i][j-1]:
                    low = False
                    continue
            if i - 1  >= 0:
                if G[i][j] >= G[i-1][j]:
                    low = False
                    continue
            
            lower.append(G[i][j] +1)
            print "i: {0}, j:{1}  {2}".format(i,j, G[i][j])

print lower

print sum(lower)

# now remove all the 9's , they do not count
# and let's visualize components

TOP = '.'

for i in range(0, max_i):
        for j in range(0, max_j):
            if G[i][j] == 9:
                G[i][j] =  TOP

def print_nice(M):
    txt =''
    for i in range(0, max_i):
        for j in range(0, max_j):
            txt = txt + str(G[i][j])
        txt = txt + '\n'

    return txt

print print_nice(G)

connected = []
visited = {}

# find connected components

for i in range(0, max_i):
    for j in range(0, max_j):
        # if not visited
        # and not a TOP
        # find size of component
        if G[i][j] != TOP and visited.get((i,j)) is None:
            q = []
            q.append((i,j))
            visited[(i,j)] = 1
            size = 1
           

            while len(q) > 0:
                (_i,_j) = q.pop()
                
                if _i -1 >=0 and G[_i-1][_j]!= TOP  and visited.get((_i-1,_j)) is None:
                    q.append((_i-1 ,_j))
                    visited[(_i-1, _j)] = 1
                    size = size + 1

                if _i + 1 < max_i and G[_i+1][_j] != TOP and visited.get((_i+1,_j)) is None:
                    q.append((_i+1, _j))
                    visited[(_i+1,_j)] = 1
                    size = size + 1
                
                if _j-1 >= 0 and G[_i][_j-1] !=  TOP and visited.get((_i, _j-1)) is None:
                    q.append((_i, _j-1))
                    visited[(_i, _j-1)] = 1
                    size = size + 1

                if _j +1  < max_j and G[_i][_j+1]!= TOP and visited.get((_i, _j+1)) is None:
                    q.append((_i, _j+1))
                    visited[(_i,_j +1)] = 1
                    size = size + 1
            # out of basin
            connected. append(size)
    

connected = sorted(connected, reverse = True)

print connected
print connected[0] * connected[1] * connected[2]
