# traveling salesman problem 
#  The first line indicates the number of cities. Each city is a point in the
#  plane, and each subsequent line indicates the x- and y-coordinates of a
#  single city.
# The distance between two cities is defined as the Euclidean distance 
import csv as csv
import math as math
import itertools;


# calculates the euclidean distance
def calculateDistance(x0,y0,x1,y1):
	d = (x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)
	d = math.sqrt(d)
	#rouding distances to nearest integer
	return int(d)

#input [1,4,0]
#output 10011
def calculateBitmask(set,B):
	_set = str(set);
	if B.get(_set)!=None:
		return B[_set]

 	bitmask = [];
	biggest = max(set)
 	for k in range(0,biggest+1):
		if k in set: 
			bitmask.append('1')
		else:
			bitmask.append('0');

	B[_set] = "".join(reversed(bitmask))	
	return B[_set];
		
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
def getSetsOfSize(s,V,sourceVertex,S):
	if S.get(s)!=None:
		return S[s]
	sets = [];
	combinations = itertools.combinations(V,s)
	for c in combinations:
		if sourceVertex in c:
			sets.append(list(c));
	S[s] = sets
	return sets

# Recurrence to find smallest path that visits a fix number of vertexes
def calculateSubsetDistance(M,G,set,destination,sourceVertex):
	print "set" +str(set)
	bitmask = calculateBitmask(set,S);
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
				_bitmask = calculateBitmask(set,S);
				_set =[i for i in set]
				distance = calculateSubsetDistance(M,G,_set,k,sourceVertex)+G[k][destination]
				candidates.append(distance)
		
			_min = min(candidates)
			M[bitmask][destination] = min(candidates)
	
	#print M	
	print "minimum distance"+str(M[bitmask][destination]);
	return  M[bitmask][destination]

f = open ('./citiesSmall.txt');
reader = csv.reader(f , delimiter=' ',quoting=csv.QUOTE_NONE);

firstRow = reader.next();

v = int(firstRow[0]); # number of vertexes

G = {} # graph with each vertex and distance to every other vertex
P = [] # stores x, y for each city
# we shall precalculate distances from anyone to anyone so each vertex will have
# 24 edges...
i = 0;

S = {} # set cache, see if it improves performance
B = {} # bitmask cache
INFINITY = 1000000;

for row in reader:
	P.append((float(row[0]),float(row[1])))
	G[i] = {};
	i = i + 1;


for j in range(len(P)):
	x0 = P[j][0];
	y0 = P[j][1];
	for k in range(len(P)):
		if k == j:
			continue
		
		x1 = P[k][0];
		y1 = P[k][1];
		d = calculateDistance(x0,y0,x1,y1);
		G[j][k] =d

#print G

# now we need to calculate the TSP values 
# remember we are numbering nodes from 0


V = G.keys()
sourceVertex = 0


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
	sets = getSetsOfSize(m,V,sourceVertex,S)
	for set in sets:
		bitmask = calculateBitmask(set,S);
		M[bitmask] = {}
		#M[bitmask][sourceVertex]= INFINITY

# for sourceVertex distance is 0
bitmask = calculateBitmask([sourceVertex],S)
M[bitmask][sourceVertex] = 0;

# now we need to add the edges that do connect with the source one
for vertex in G[sourceVertex].keys():
	bitmask = calculateBitmask([sourceVertex,vertex],S);
	M[bitmask][vertex] = G[sourceVertex][vertex]


#print M
#print G

print "starting dynamic programing algorithm------"

for m in range(2,v+1):
	sets = getSetsOfSize(m,V,sourceVertex,S)
	for set in sets:
		bitmask = calculateBitmask(set,S)
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
				if k==sourceVertex:
					continue
				_set =[i for i in set]
				candidate = calculateSubsetDistance(M,G,_set,j,sourceVertex)
				candidates.append(candidate);
			#print M	
			M[bitmask][j] = min(candidates)  


#print M

# now we need to calculate the last hop, coming back to 1 from j
# what is the set that minimizes this value?
# using all sets of size v
sets = getSetsOfSize(v,V,sourceVertex,S);

lastHopCandidates = []
for set in sets:
 bitmask = calculateBitmask(set,S);
 print "looking up bitmask"+bitmask
 #rememeber we are numbering vertexes starting at 0
 for j in range(1,v):
	if G[j][sourceVertex]!= None:
		candidate = M[bitmask][j]+G[j][sourceVertex];
		print "for vertex"+str(j)
		print "candidate is"+str(candidate)
		lastHopCandidates.append(candidate)


print "candidates"
print lastHopCandidates

print min(lastHopCandidates);
 





