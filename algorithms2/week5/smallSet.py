# try to solve TSP for a smaller graph
# using dynamic programing approach
# not an obvious algorithm, look at lecture
# we assume every vertex is reachable from any other one
import csv as csv
import itertools;


def calculateBitmask(set):
 	bitmask = [];
	biggest = max(set)
 	for k in range(0,biggest+1):
		if k in set: 
			bitmask.append('1')
		else:
			bitmask.append('0');

	return "".join(reversed(bitmask));
		
def undoBitmask(bitmask):
	_bitmask = [int(i) for i in bitmask]
	set =[];
	l = len(_bitmask);

	for k in range(l):
		if _bitmask[l-1-k] == 1: 
			set.append(k)
	return set;	

# returns the different possible sets of size s
# out of set v
# every set contains vertex 1
def getSetsOfSize(s,V,sourceVertex):
	sets = [];
	combinations = itertools.combinations(V,s)
	for c in combinations:
		if sourceVertex in c:
			sets.append(list(c));
	return sets

# Recurrence to find smallest path that visits a fix number of vertexes
def calculateSubsetDistance(M,G,set,destination,sourceVertex):
	print "set" +str(set)
	bitmask = calculateBitmask(set);
	print "destination"+str(destination)

	# do not recalculate if we alreday did it
	if M.get(bitmask).get(destination)==None:
		print "calculating ..."
		candidates =[]
		# if there is only two elements  
		if len(set) == 2:
			M[bitmask][destination] = G[sourceVertex][destination]
		else:
			# candidate set is bigger
			# do brute force search from 1 to k k to j
			set.remove(destination)
			for k in set:
				print "k="+str(k)
				if k==sourceVertex or k==destination:
					continue
				_bitmask = calculateBitmask(set);
				_set =[i for i in set]
				distance = calculateSubsetDistance(M,G,_set,k,sourceVertex)+G[k][destination]
				candidates.append(distance)
		
			_min = min(candidates)
			M[bitmask][destination] = min(candidates)
	
	#print M	
	print "minimum distance"+str(M[bitmask][destination]);
	return  M[bitmask][destination]

					
f  = open('./testCase1.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

# each vertext points to edges incident on it
G = {}; #hasmap,represents graph, each vertex is a hashmap
		#A[B]=2,A[C]=3
		#B[A]= 2
		#C[A] =3

firstRow = reader.next();
v = int(firstRow[0]);
INFINITY = 1000000;
for row in reader: 
	n1 = int(row[0])
	n2 = int(row[1])
	distance = int(row[2])
	if G.get(n1)==None:
		G[n1] = {};
	G[n1][n2] = distance;

V = G.keys()
sourceVertex = 1
# number of sets
# combinations of v-1 items (all need to include vertex 1)
# in groups of 2..n
# need to calculate this, in the testCase1 the number of subsets is 6 


#testing bitmasks
#b = calculateBitmask([1,2,3])
#print "bitmask 1,2,3 "+str(b)
#print undoBitmask(b)

#b = calculateBitmask([1,4])
#print "bitmask 1,4 "+str(b)
#print undoBitmask(b)

#b = calculateBitmask([1,3])
#print "bitmask 1,3 "+str(b)
#print undoBitmask(b)



M ={}#using a hash rather than an array
# base cases
for m in range(1,v+1):
	sets = getSetsOfSize(m,V,sourceVertex)
	for set in sets:
		bitmask = calculateBitmask(set);
		M[bitmask] = {}
		M[bitmask][sourceVertex]= INFINITY

# for sourceVertex distance is 0
bitmask = calculateBitmask([sourceVertex])
M[bitmask][sourceVertex] = 0;

# now we need to add the edges that do connect with the source one
for vertex in G[sourceVertex].keys():
	bitmask = calculateBitmask([sourceVertex,vertex]);
	M[bitmask][vertex] = G[sourceVertex][vertex]


print M
print G

for m in range(2,v+1):
	sets = getSetsOfSize(m,V,sourceVertex)
	for set in sets:
		bitmask = calculateBitmask(set)
		for j in set:
			if j==sourceVertex:
				continue
			print ">>>>>j= "+str(j)
			candidates = []
			# calculate the path to 'j' from 1 given a budget
			# of m edges that are specified in set
			#print "j"+str(j)
			# candidate set is bigger
			# do brute force search from 1 to k k to j
			
			for k in set:
				if k==1:
					continue
				_set =[i for i in set]
				candidate = calculateSubsetDistance(M,G,_set,j,sourceVertex)
				candidates.append(candidate);
			
			M[bitmask][j] = min(candidates)  


print M

# now we need to calculate the last hop, coming back to 1 from j
# what is the set that minimizes this value?
# using all sets of size v
sets = getSetsOfSize(v,V,sourceVertex);

lastHopCandidates = []
for set in sets:
 bitmask = calculateBitmask(set);
 print "looking up bitmask"+bitmask
 for j in range(2,v+1):
	if G[j][sourceVertex]!= None:
		candidate = M[bitmask][j]+G[j][sourceVertex];
		print "for vertex"+str(j)
		print "candidate is"+str(candidate)
		lastHopCandidates.append(candidate)


print "candidates"
print lastHopCandidates

print min(lastHopCandidates);
 
