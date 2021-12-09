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
                if G[i][j] > G[i][j+1]:
                    low = False
                    continue
            if i+ 1 < max_i:
                if G[i][j] > G[i+1][j]:
                    low = False
                    continue
            if j - 1 >= 0:
                if G[i][j] > G[i][j-1]:
                    low = False
                    continue
            if i - 1  >= 0:
                if G[i][j] > G[i-1][j]:
                    low = False
                    continue
            lower.append(G[i][j])


print lower

print sum(map(lambda x: x+1, lower))




