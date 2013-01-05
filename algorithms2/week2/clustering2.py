
#In this question your task is again to i
#run the clustering algorithm from lecture, 
#but on a MUCH bigger graph. 
#So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.
#The data set is here. The format is:
#[# of nodes] [# of bits for each node's label]
#[first bit of node 1] ... [last bit of node 1]
#[first bit of node 2] ... [last bit of node 2]
#For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.
#The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

#The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?


import csv as csv
import heapq as hp

# will find out whether this new edge starts a cluster of its own 
# or rather fuses two clusters or plainly gets added to a new cluster
# might modify the cluster set and thus it is returned
# is there a better data structure? this works but ...
def addNewEdgeToClusterSet(clusters,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	fuse =[]
	notFuse =[]
	
	for cluster in clusters:
		if doesEdgeBelongToCluster(cluster,edge):
			fuse.append(cluster);
		else:
			notFuse.append(cluster);


	if len(fuse)>0:
		clusters = notFuse;
		#merge the dictionaries
		if len(fuse)>1:
			f = {}
			for i in range(len(fuse)):
				f.update(fuse[i])
		else:
			f = fuse[0]
		f = addNodeToGraph(f,distance,n1,n2)
		clusters.append(f);
	else: 
		# edge should be added to a cluster of its own
		# doesn't seem to be in any cluster 
		C = {};
		C = addNodeToGraph(C,distance,n1,n2);
		clusters.append(C);



	return clusters


def doesEdgeBelongToCluster(cluster,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	if(cluster.get(n1)==None and cluster.get(n2)==None):
		return False;
	else:
		return True;
	
def addNodeToGraph(G,distance,n1,n2):
	if G.get(n1)==None:
		G[n1] = [];
	G[n1].append((n2,distance))

	if G.get(n2) == None:
		G[n2] = [];
	G[n2].append((n1,distance))
	return G

# calculate hamming distance uaing strings
# converts each string to an array and calculates 
# distance by comparing each character
def hamming_distance(s1, s2):
	if s1 == s2:
		return 0
	sum = 0
	for ch1, ch2 in zip(s1, s2):
		if ch1 != ch2:
			sum = sum +1
			if sum >3:
				#exit early
				return sum
	return sum



					
f  = open('./clustering2.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

# each vertext points to edges incident on it
G = {}; #hasmap,represents graph, each vertex is an index
		# each index has an array of vertexes
		#A : [(B,2),(C,3)]
		#B: [(A,2)]
		#C:[(A,3)]

clusters =[]; # we know size of clusters has to be 4 maximum


h =[];# heap that will store edges by distance
nodes = []; #nodes array

#read all nodes
for row in reader: 
	n1 = row[0]
	n1.strip()
	nodes.append(n1)	

# we really only need to calculate distances
# up to three, nodes that are further appart than that we can disregard
l = len(nodes)

# to use this you need to remove duplicates
for i in range(l):
	n1 = nodes[i]
	
	for j in range(i+1,l):
		n2 = nodes[j]
		distance = hamming_distance(n1,n2)
		if distance <=3:
			print n1,n2,distance
			G = addNodeToGraph(G,distance,n1,n2);
			hp.heappush(h,(distance,[n1,n2]))

#now we have all data into a graph
size = len(G)
print G

#nodes that we know will not be clustered
standAloneNodes = len(nodes)-len(G)

print "stand Alone nodes"
print standAloneNodes

print " Created heap and graph";

actualNumberOfClusters = len(G);


distance = 0
maxDistance =3
#whether we are at the beginning or we have a distance less than minimum
while (len(clusters)==0 or distance <=maxDistance) and len(h)>0:
	startClusters = len(clusters)+len(G)
	edge = hp.heappop(h);
	clusters = addNewEdgeToClusterSet(clusters,edge)
	distance = edge[0];
	n1 = edge[1][0];
	n2 = edge[1][1];

	# delete nodes from main graph if pertains  which is the last cluster
	if (G.get(n1)!=None):
		del G[n1]		
	if (G.get(n2)!=None):
		del G[n2]
	endClusters = len(clusters)+len(G)
	if distance == maxDistance and startClusters >endClusters:
		finalClusters = startClusters
		break
	elif len(h)==0:
		finalClusters = endClusters



print "last item joined two clusters, so max distance is 3 when we have"
print finalClusters
print "stand alone"
print standAloneNodes
print "total number of clusters"
print standAloneNodes+finalClusters
exit()





