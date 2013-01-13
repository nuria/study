
#The first line indicates the number of vertices and edges, respectively. 

# Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) 
# 1 14 6" represent an edge from 1 to 14 with length 6
# tail:1, head:14 weight:6
# and its length (the third number). NOTE: some of the edge lengths are
# negative.NOTE: These graphs may or may not have negative-cost cycles.

#Your task is to compute the "shortest shortest path". 
#Precisely, you must first identify which, if any, of the three graphs have no negative cycles.
import csv as csv;

# for jhonson's algorithm, adds an 's' edge
# with edge cost 0
# since we are keeping track of graph like
# G[head][tail]
# we are adding a G[s][v] =0  for all Vertexes v in G
def addSVertex(G,v):
	vertexes = G.keys()
	v =  v+1;#assuming sequential indexes 
	G[v] ={}
	for w in vertexes:
		G[w][v] = 0
	return G,v


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

G,v = addSVertex(G,v) #can identify vertex by v+1

print G


#print G
infinity = 1000000;

M =  [[infinity for w in range(v+1)] for i in range(2)] #space optimization,keep only two rows

#We will calculate shortest paths from S
sourceVertex = v;
M[0][v] = 0;

destinationSet = G.keys();

#print destinationSet

# Bellman Ford,running it for v iterations
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
		break

# no cycle

print prior
print last 

