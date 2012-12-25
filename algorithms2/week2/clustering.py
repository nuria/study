
#In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. Download the text file here. This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
# [number_of_nodes]
#[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
#[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
#There is one edge (i,j) for each pair 

#Your task in this problem is to run the clustering algorithm 
#from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?


import csv as csv
import heapq as hp

# will find out whether this new edge starts a cluster of its own 
# or rather fuses two clusters or plainly gets added to a new cluster
# might modify the cluster set and thus it is returned

def addNewEdgeToClusterSet(clusters,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	
	print "Initial clusters keys"
	for c in clusters:
		print c.keys();

	fuse =[]
	notFuse =[]
	
	for cluster in clusters:
		if doesEdgeBelongToCluster(cluster,edge):
			fuse.append(cluster);
		else:
			notFuse.append(cluster);


	if len(fuse)>0:
		#print "We need to fuse the following clusters"
		#print fuse;
		#print "with"
		#print edge
		clusters = notFuse;
		#merge the dictionaries
		if len(fuse)>1:
			f = {}
			for i in range(len(fuse)):
				f.update(fuse[i])
				print f
		else:
			f = fuse[0]
		f = addNodeToGraph(f,distance,n1,n2)
		clusters.append(f);
	else: 
		# edge should be added to a cluster of its own
		# doesn't seem to be in any cluster 
		C = {};

		print "Adding node to its own graph"
		C = addNodeToGraph(C,distance,n1,n2);
		clusters.append(C);


	print "Resulting clusters keys"
	for c in clusters:
		print c.keys();

	return clusters


def doesEdgeBelongToCluster(cluster,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	#print "Do nodes"
	#print n1
	#print n2
	#print "belong to cluster"
	#print cluster
	if(cluster.get(n1)==None and cluster.get(n2)==None):
		#print "no"
		return False;
	else:
		#print 'yes'
		return True;
	
def addNodeToGraph(G,distance,n1,n2):
	if G.get(n1)==None:
		G[n1] = [];
	G[n1].append((n2,distance))

	if G.get(n2) == None:
		G[n2] = [];
	G[n2].append((n1,distance))
	return G




k = 4; 
					
f  = open('./clustering.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

# each vertext points to edges incident on it
G = {}; #hasmap,represents graph, each vertex is an index
		# each index has an array of vertexes
		#A : [(B,2),(C,3)]
		#B: [(A,2)]
		#C:[(A,3)]

clusters =[]; # we know size of clusters has to be 4 maximum


h =[];# heap that will store edges by distance

for row in reader: 
	n1 = int(row[0])
	n2 = int(row[1])
	distance = int(row[2])
	G = addNodeToGraph(G,distance,n1,n2);
	hp.heappush(h,(distance,[n1,n2]))



#now we have all data into a graph

size = len(G)

print " Created heap and graph";
#print G

actualNumberOfClusters = len(G);


while  actualNumberOfClusters > 4:
	edge = hp.heappop(h);
	clusters = addNewEdgeToClusterSet(clusters,edge)
	distance = edge[0];
	n1 = edge[1][0];
	n2 = edge[1][1];

	# delete nodes from main graph if pertains  which is the last cluster
	if (G.get(n1)!=None):
		del G[n1]		
		#print "deleting" 
		#print n1
	if (G.get(n2)!=None):
		#print "deleting"
		#print n2
		del G[n2]
	actualNumberOfClusters = len(clusters)+len(G)
		


print "final set of clusters"
#print clusters;
#now append whatever is left in G



list = G.keys() ; # each key would be a cluster

for l in list:
	C = {}
	C[l] = G[l]
	clusters.append(C)

# out of curiosity print the number of nodes of each cluster

print "number of nodes in each cluster"

for cluster in clusters:
	nodes = cluster.keys()
	print nodes


# keep pulling from heap, 1st edge that crossses the cut
# is the maximun distance
distance =0;

#print h

found = False;
while True and not found:
	edge = hp.heappop(h)
	distance = edge[0];
	n1 = edge[1][0];
	n2 = edge[1][1];
	print edge;
	for cluster in clusters:
		nodes = cluster.keys()
		print 'nodes'
		print nodes
		print 'n1'
		print cluster.get(n1); 
		print 'n2'
		print cluster.get(n2)
		if (cluster.get(n1)==None and cluster.get(n2)!=None ) or (cluster.get(n2)==None and cluster.get(n1)!=None): 
			found = True;
		



print "distance"
		
print distance;
