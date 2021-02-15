#!usr/local/bin
f= open('./test_input3.txt')

# the grid
G = []

for l in f:
	l = l.strip()
	items = list(l)
	#print items
	G.append(items)

max_x = len(G[0]) - 1
max_y = len(G) -1

print "max x"
print max_x

print "max y"
print  max_y

trees = 0
# right 3, down 1

x = 0
y = 0

TREE = '#'

while(y < max_y):
	# going down
	x = x + 3	
	if  x > max_x :
		x = x -max_x - 1
	y = y + 1 

	#print "{0}, {1}".format(x,y)

	# add tree if you landed on one 	
	if G[y][x] == TREE:
		trees+=1
print "trees"
print trees
