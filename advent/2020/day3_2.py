#!usr/local/bin
f= open('./input3.txt')

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


TREE = '#'

def count_trees(delta_x, delta_y):
	trees = 0
	x = 0
	y = 0

	while(y+delta_y <= max_y):
		# going down
		x = x + delta_x
		if  x > max_x :
			x = x -max_x - 1
		y = y + delta_y

		#print "{0}, {1}".format(x,y)

		# add tree if you landed on one 	
		if G[y][x] == TREE:
			trees+=1

	return trees


trees = count_trees(1,1) * count_trees(3,1)* count_trees(5,1) * count_trees(7, 1) * count_trees(1,2)

print trees
