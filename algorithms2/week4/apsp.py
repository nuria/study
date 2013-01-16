
#The first line indicates the number of vertices and edges, respectively. 

# Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) 
# 1 14 6" represent an edge from 1 to 14 with length 6
# tail:1, head:14 weight:6
# and its length (the third number). NOTE: some of the edge lengths are
# negative.NOTE: These graphs may or may not have negative-cost cycles.

#Your task is to compute the "shortest shortest path". 
#Precisely, you must first identify which, if any, of the three graphs have no negative cycles.
import csv as csv;
import heapq as hp;

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

# initialize heap with distances from s to the rest of nodes in G
# graph
# we are building the heap everytime
# should improve that
# distances calculated so far
def buildHeap(G,X,s,D):
 h = []
 infinity = INFINITY
 print X
 for head in G.keys():
	#skip vertexes already in X
	if X.get(head)!=None:
		continue;
	for  tail in G.get(head).keys():
		if D[tail]!= INFINITY:
			cost = D[tail] + G[head][tail]	
		else:
			cost = INFINITY
		hp.heappush(h,(head,cost));


 return h;
		

# returns shortest paths from all vertexes to vertex s
def dijistra(G,s,v):
	X = {}; # explored nodes
	D = []
	#initialize all = INFINITY
	# note array is off is calculating distances from '0'
	for i in range(v+1):
		D.append(INFINITY);
	D[s] = 0
	X[s] =1;
	h = buildHeap(G,X,s,D);
	while len(X)!= v :
		if len(h)<1:
			print "Exiting, some nodes were not rechable."
			break
		min = hp.heappop(h);
		vertex = min[0];
		cost = min[1];
		D[vertex]  = cost;
		X[vertex] = 1;
		h = buildHeap(G,X,s,D)

	
	return D; 

#----------------------------  main program ---------------------


f = open('./testCase1.txt','rb');
reader = csv.reader(f,delimiter=' ',quoting=csv.QUOTE_NONE); 


firstRow = reader.next();

v = int(firstRow[0]);#number of vertexes
e = int(firstRow[1]); #number of edges

G = {}
for row in reader: 
	#build adjacency list,keeping pointers like:
	# G[head][tail] = weight
	#tail ---->head
	tail = int(row[0])
	head = int(row[1])
	weight = int(row[2])
	if G.get(tail)==None:
		G[tail] = {};
	if G.get(head)==None:
		G[head] = {}
	
	G[head][tail]= weight;

# now add S vertex
print "Original graph"
print G
G,v = addSVertex(G,v) #can identify vertex by v+1
print "G+s vertex"
print G
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

print G


# Dijistra now. 
# we need to run it for all vertexes, trying one for now

B = dijistra(G,1,v)

print B

