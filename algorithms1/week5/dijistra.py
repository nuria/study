
#The first line indicates the number of vertices and edges, respectively. 

import csv as csv;
import heapdict as hpdict;
INFINITY = 100000;
 #Each row consists of the node tuples that are adjacent 
 #to that particular vertex along with the length of that edge. 
 #For example, the 6th row has 6 as the first entry indicating 
 #that this row corresponds to the vertex labeled 6. 
 #The next entry of this row "141,8200" indicates that 
 #there is an edge between vertex 6 and vertex 141 
 #that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent 
 #to vertex 6 and the lengths of the corresponding edges.
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

#f = open('./g3.txt','rb');
f = open('./dijistraData.txt','rb');
reader = csv.reader(f,delimiter='\t',quoting=csv.QUOTE_NONE); 




G = {}
T = {}
for row in reader: 
	#build adjacency list,keeping pointers like:
	#tail ---->head
	# we are assuming the graph could be directed
	# although i think this particular output is not
	tail = int(row[0])
	for i in range(1,len(row)):
		row[i].rstrip();
		pair = row[i].split(',');
		if pair[0].isdigit():
			head = int(pair[0])
			weight = int(pair[1])
			
			if G.get(head)==None:
				G[head] = {}
			G[head][tail]= weight;
			
			if G.get(tail)==None:
				G[tail] ={}
			G[tail][head] = weight;

			if T.get(tail)==None:
				T[tail] = []
			T[tail].append(head)

#print G

# Dijistra now. 
# in order to run dijistra we need to be able to look outgoing vertexes
# from a given one (in G we are storing incoming vertexes to head like
# G[head][tail]
# we need a reverse lookup T[tail][head]
# we need to run it for all vertexes, trying one for now
sourceVertex = 1
v= len(G)
B = dijistra(G,T,sourceVertex,v)

print "distances from source vertex: "+ str(sourceVertex)
for i in range(len(B)):
	print "To: "+str(i)+" "+str(B[i])
