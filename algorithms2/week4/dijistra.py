
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
# s = source vertex we have added to X set
def bootstrapHeap(G,s):
 h = hpdict.heapdict();

 for head in T[s]:
	cost = G[head][s]	
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
	# if vertext does not have any outfoing edges 
	# we can return
	if T.get(s) == None:
		return D
	hp = bootstrapHeap(G,s);
	while len(hp) > 0:
		smallest = hp.popitem();
		w = smallest[0];
		cost = smallest[1];
		if explored.get(w) != None:
			continue

		#print "Adding vertex into explored:"+str(w)
		#print "with distance: "+str(cost)
		D[w]  = cost;
		explored[w] = 1;
		# now update values on heap
		# get all edges outgoing from 'w'
		# if vertext at head of edge is not explored
		#	update cost
		# if head is explored, remove from heap
		if T.get(w)==None:
			#print str(w)+" has no outgoing edges"
			continue
		for v in T.get(w):
			#print "---Checking vertext "+str(v)
			if explored.get(v)==None:
				# if the node is not the heap yey
				newCost = D[w]+G[v][w]
				if hp.get(v)==None or newCost < hp[v]:
					#only update cost if it is lower
					hp[v]= newCost

				#print "---updating cost for vertex "+str(v)
				#print "----- to cost"+str(hp[v])
			elif hp.get(v)!=None: 
				del hp[v]
		#print heapToString(hp)
	return D; 


#----------------------------  main program ---------------------
# Runing Jhonson's algorirthm to find shortest paths

#f = open('./g3.txt','rb');
f = open('./testCase2.txt','rb');
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



# Dijistra now. 
# in order to run dijistra we need to be able to look outgoing vertexes
# from a given one (in G we are storing incoming vertexes to head like
# G[head][tail]
# we need a reverse lookup T[tail][head]
# we need to run it for all vertexes, trying one for now
sourceVertex = 1
B = dijistra(G,T,sourceVertex,v)

print "distances from source vertex: "+ str(sourceVertex)
for i in range(len(B)):
	print "From: "+str(i)+" "+str(B[i])
