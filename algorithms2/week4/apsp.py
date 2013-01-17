
#The first line indicates the number of vertices and edges, respectively. 

# Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) 
# 1 14 6" represent an edge from 1 to 14 with length 6
# tail:1, head:14 weight:6
# and its length (the third number). NOTE: some of the edge lengths are
# negative.NOTE: These graphs may or may not have negative-cost cycles.

#Your task is to compute the "shortest shortest path". 
#Precisely, you must first identify which, if any, of the three graphs have no negative cycles.
import csv as csv;
import heapdict as hpdict;

INFINITY = 100000;
# for jhonson's algorithm, adds an 's' edge
# with edge cost 0
# since we are keeping track of graph like
# G[head][tail] (tail) ------> (head)
# we are adding a G[s][v] =0  for all Vertexes v in G
def addSVertex(G,v):
	vertexes = G.keys()
	v =  v+1;#assuming sequential indexes 
	G[v] ={}
	for w in G.keys():
		G[w][v] = 0
	return G,v


def removeSVertex(G,v):
	del G[v]
	for w in G.keys():
		del G[w][v]
	v = v-1
	return G,v

# toString method is not in heapdict
def heapToString(h):
	msg =" heap {"
	for i in h.keys():
		msg = msg +" "+str(i)+" :"+str(h[i])
	return msg+"}"

# heap with distances from s to the rest of nodes in G
# graph
# Using a heap from which we 
# can access items like a hashmap
# s=vertex we have added to X set
# D= distances calculated so far
def buildHeap(G,s,D):
 h = hpdict.heapdict();
 h[s] = 0
 for head in G.keys():
	#skip vertexes in X
	if head == s:
		continue;
	for  tail in G.get(head).keys():
		if D[tail]!= INFINITY:
			cost = D[tail] + G[head][tail]	
		else:
			cost = INFINITY
		h[head] = cost;

 #print heapToString(h)
 return h;


# returns shortest paths from all vertexes to vertex s
# G graph G[head][tail]= weight
# T G[tail] = [] , outgoing edges from a tail
def dijistra(G,T,s,v):
	D = []
	explored = {} #TODO , can we save this explored set and use distances!=INFINITY
	#initialize all = INFINITY
	# note array is off is calculating distances from '0'
	for i in range(v+1):
		D.append(INFINITY);
	D[s] = 0
	explored[s] = 1
	hp = buildHeap(G,s,D);
	while len(hp) > 0:
		smallest = hp.popitem();
		w = smallest[0];
		cost = smallest[1];
		#print "Adding vertex into explored:"+str(w)
		#print "with distance: "+str(cost)
		D[w]  = cost;
		explored[w] = 1;
		# now update values on heap
		# get all vertexes outgoing from 'w'
		# if head of vertex in heap (not explored)
		#	update cost
		# if head is explored, remove from heap
		if T.get(w)==None:
			#head has no outgoing edges
			#print str(w)+" has no outgoing edges"
			continue
		for v in T.get(w):
			#print "---updating cost for vertex "+str(v)
			if explored.get(v)==None:
				if D[w]==INFINITY:
					hp[v] = INFINITY
				else:
					hp[v]=D[w]+G[v][w]
				#print "----- to cost"+str(hp[v])	
		#print heapToString(hp)
	return D; 

#----------------------------  main program ---------------------
# Runing Jhonson's algorirthm to find shortest paths

#f = open('./g3.txt','rb');
f = open('./testCase1.txt','rb');
reader = csv.reader(f,delimiter=' ',quoting=csv.QUOTE_NONE); 


firstRow = reader.next();

v = int(firstRow[0]);#number of vertexes
e = int(firstRow[1]); #number of edges

G = {}
T = {}
for row in reader: 
	#build adjacency list,keeping pointers like:
	# G[head][tail] = weight
	# T[tail] = [] , this T lookup will be useful in dijistra
	# space optimization , if tail has no outgoing edges is not present on T
	#tail ---->head
	tail = int(row[0])
	head = int(row[1])
	weight = int(row[2])
	if G.get(tail)==None:
		G[tail] = {};
	if G.get(head)==None:
		G[head] = {}
	
	G[head][tail]= weight;

	if T.get(tail)==None:
		T[tail] = []
	T[tail].append(head)

# now add S vertex
print "Original graph"
#print G
G,v = addSVertex(G,v) #can identify vertex by v+1
print "G+s vertex"
#print G
#print G


#print G
infinity = INFINITY

M =  [[infinity for w in range(v+1)] for i in range(2)] #space optimization,keep only two rows

#We will calculate shortest paths from S
sourceVertex = v;
M[0][v] = 0;

destinationSet = G.keys();

#print destinationSet

# Bellman Ford algorithm running it for v iterations
# to see if there is a cycle
for i in range(1,v+1):
	for vertex in destinationSet:
		# all edges that end at vertex
		vSet = G[vertex];
		d = infinity;
		# space optimization,only working with two rows
		if i % 2 ==0:
			i = 0
		else:
			i = 1
		for w in vSet.keys():
			if M[i-1][w]==infinity:
				tmp = infinity
			else:
				tmp = M[i-1][w]+G[vertex][w];
			d = min(d,tmp)
		
		d = min(d,M[i-1][vertex])
		M[i][vertex] = d
			
# look to see if there is a cycle on resul matrix
# iterate on matrix, if there is no cycle A[n-1,v] == A[n,v]
# with our space optimization we only have two rows

if v % 2 ==0:
	last = M[0]
	prior = M[1]
else:
	last = M[1]
	prior = M[0]


for j in range(len(last)):
	if last[j] != prior[j]:
		print "cycle!!!"
		raise SystemExit

# no cycle

print "Here are the mins"
print prior
print min(prior)
print min(last)

# Reweighting
# Pv = M[v]
# Get graph without "s" vertex
G,v = removeSVertex(G,v)
for head in G.keys():
	for tail in G[head].keys():
		G[head][tail] = G[head][tail]+last[tail]-last[head]
		if G[head][tail] < 0:
			print "Error! negative lengths after reweighting graph";
			raise SystemExit
print "Graph after reweight"
#print G


# Dijistra now. 
# in order to run dijistra we need to be able to look outgoing vertexes
# from a given one (in G we are storing incoming vertexes to head like
# G[head][tail]
# we need a reverse lookup T[tail][head]
# we need to run it for all vertexes, trying one for now
minPath = INFINITY
minPathOriginal = INFINITY
for sourceVertex in range(1,v+1):
	print ">>distances from source vertex"+str(sourceVertex)
	B = dijistra(G,T,sourceVertex,v)
	tmpMin = min(B)
	if tmpMin < minPathOriginal:
		minPathOriginal = tmpMin
	#print B
	for w in range(len(B)):
		if B[w]==INFINITY:
			continue
		B[w] =  B[w]+last[sourceVertex]-last[i]
	#print B
	shortestPath = min(B)
	if shortestPath < minPath:
		minPath = shortestPath
	print "min path for now"+str(minPath)

print "shortest shortest path:"
print minPath

print "min path original"
print minPathOriginal

