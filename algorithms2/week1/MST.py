
# file with 500 nodes and hudresd of edges
# n1, n2 , edge cost
# write algorithm that calculates cost of MST


import csv as csv
import heapq as hp



def getHeapLowerCostEdge(X,G):
	h =[]
	keys = X.keys();
	_edges = []# really tuples of node,cost
	for key in keys:
		edges = G[key]
		for edge in edges:
			_node = edge[0]
			if X.get(_node)==None:
				_edges.append(edge);

	for edge in _edges:
		node = edge[0]
		cost = edge[1]
		#add edge to heap
		hp.heappush(h,(cost,node))
	
	return h




					
f  = open('./MSTdata.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

# each vertext points to edges incident on it
G = {}; #hasmap,represents graph, each vertex is an index
		# each index has an array of vertexes
		#A : [(B,2),(C,3)]
		#B: [(A,2)]
		#C:[(A,3)]

#each edge points to its end points
edges =[]

X = {} # explored nodes, set

# not most efficient implementation

for row in reader: 
	n1 = int(row[0])
	n2 = int(row[1])
	cost = int(row[2])
	if G.get(n1)==None:
		G[n1] = [];
	G[n1].append((n2,cost))

	if G.get(n2) == None:
		G[n2] = [];
	G[n2].append((n1,cost))


#now MST

size = len(G)

print "G -----";
#print G

# we have to start somewhere, starting at node 1
X[1] = [];# using a hashmap for lookups
	      # not sure if you can do lookups in a set


node = 1
MST = 0
while size > len(X): 	
	edges = G[node]
	print"X---"
	print X

	print "edges"
	print edges;

	# this heap will contain only edges
	# that do not go into nodes in X
	h = getHeapLowerCostEdge(X,G);
	# if heap is empty we have reached the end or a point where
	# we need to pick another random node
	if len(h) <1:
		if size-1 == len(X):
			break
	
	#elements have been pushed into the heap like this: hp.heappush(h,(cost,node))
	lowest = hp.heappop(h)
	newNode = lowest[1]
	MST = MST+lowest[0]


	X[newNode] = []; # using a hashmap for lokups
	node = newNode

print"X-----";
print X
print MST






