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
	return d


def calculateBitmask(s,B,destination):
	_set = "".join(str(e) for e in s);
	#print "_set"+_set
	if B.get(_set)!=None:
		return B[_set]
	bitmask = _set+str(destination)
	#print bitmask
	return int(bitmask)



#input [1,4,0]
#output 10011
def calculateBitmaskBimary(set,B):
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


f = open ('./citiesSmall.txt');
reader = csv.reader(f , delimiter=' ',quoting=csv.QUOTE_NONE);

firstRow = reader.next();

v = int(firstRow[0]); # number of vertexes

G = {} # graph with each vertex and distance to every other vertex
P = [] # stores x, y for each city
# we shall precalculate distances from anyone to anyone so each vertex will have
# 24 edges...
i = 1;

S = {} # set cache, see if it improves performance
B = {} # bitmask cache
INFINITY = 1000000;

for row in reader:
	P.append((float(row[0]),float(row[1])))
	G[i] = {};
	i = i + 1;


V = G.keys()

for j in range(len(P)):
	x0 = P[j][0];
	y0 = P[j][1];
	for v in V:
		if v == j+1: #no need to calculate distance to itself
			continue
		x1 = P[v-1][0]; 
		y1 = P[v-1][1];
		d = calculateDistance(x0,y0,x1,y1);
		G[v][j+1] =d

#print G

# now we need to calculate the TSP values 
# remember we are numbering nodes from 0


sourceVertex = 1


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



# memory improvement: use 1 dimensional structure

# for sourceVertex distance is 0

M1 = {};
M2 = {};
#M1[bitmask] = 0

# now we need to add the edges that do connect with the source one
for vertex in G[sourceVertex].keys():
	bitmask = calculateBitmask([sourceVertex,vertex],S,vertex);
	#print "inserting bitmask "+str(bitmask)
	M1[bitmask]=G[sourceVertex][vertex]


#print M1
#print G

print "starting dynamic programing algorithm------"

# working with two arrays for memonization scheme
for m in range(3,v+1):
	sets = getSetsOfSize(m,V,sourceVertex,S)
	# for memonization scheme
	if m % 2 != 0: 
		M2 = {} #current
		C = M2
		P = M1 #prior
	else:
		M1 = {}#current
		C = M1
		P = M2 #prior
	#print P
	#print C
	for set in sets:
		#print ">>>>>set"+str(set)
		for j in set:
			if j==sourceVertex:
				continue
			#print ">>>>>j= "+str(j)
			candidates = []
			# calculate the path to 'j' from 1 given a budget
			# of m edges that are specified in set
			#print "j"+str(j)
			# candidate set is bigger
			# do brute force search from 1 to k k to j
			bitmask = calculateBitmask(set,B,j)
			for k in set:
				if k==sourceVertex or k == j:
					continue
				_set =[i for i in set]
				#print _set
				_set.remove(j)
				_bitmask = calculateBitmask(_set,B,k)
				#print "k"+str(k)
				#print "j"+str(j)
				#print "bitmask"+str(_bitmask)
				#print P[_bitmask]
				candidate = P[_bitmask] + G[k][j]
				candidates.append(candidate);

			C[bitmask] = min(candidates);
			#print ">>>> Current"
			#print C	


#print M

# now we need to calculate the last hop, coming back to 1 from j
# what is the set that minimizes this value?
# using all sets of size v
sets = getSetsOfSize(v,V,sourceVertex,S);

lastHopCandidates = []
for set in sets:
 for j in range(sourceVertex+1,v+1):
	bitmask = calculateBitmask(set,S,j);
	candidate = C[bitmask]+G[j][sourceVertex];
	print "for vertex"+str(j)
	print "candidate is"+str(candidate)
	lastHopCandidates.append(candidate)


print "candidates"
print lastHopCandidates

print min(lastHopCandidates);
 





