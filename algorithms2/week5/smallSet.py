# try to solve TSP for a smaller graph
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


def calculateSubsetDistance(M,G,set,destination,sourceVertex):
	
	bitmask = calculateBitmask(set);
	candidates = [];
	print "bitmask"+bitmask
	print "destination"+str(destination)
	if M.get(bitmask).get(destination)!=None:
		return M[bitmask][destination]

	# if there is only one element 
	if len(set) == 2:
		bitmask = calculateBitmask([sourceVertex]);
		if G[sourceVertex][destination]!=None:
			M[bitmask][destination] = G[sourceVertex][destination]
		else: 
			M[bitmask][destination] = INFINITE

		distance = M[bitmask][j]
		candidates.append(distance)
	else:
		# candidate set is bigger
		# do brute force search from 1 to k k to j
		set.remove(destination)
		for k in set:
			if k==sourceVertex:
				continue
			_set =[i for i in set]
			if G[k][destination]!=None:
				print "removing k= "+str(k)+"from set:"
				print _set
				_set.remove(k);
				_bitmask = calculateBitmask(_set);
				print "Set "+_bitmask
				print M
				distance = calculateSubsetDistance(M,G,_set,k,sourceVertex)+G[k][destination]
				candidates.append(distance)
	return min(candidates)


					
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
b = calculateBitmask([1,2,3])
print "bitmask 1,2,3 "+str(b)
print undoBitmask(b)

b = calculateBitmask([1,2,4])
print "bitmask 1,2,4 "+str(b)
print undoBitmask(b)


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
	M[bitmask][vertex] = G[sourceVertex][vertex]


print M
print G

for m in range(2,v+1):
	sets = getSetsOfSize(m,V,sourceVertex)
	for set in sets:
		print set
		for j in set:
			if j==sourceVertex:
				continue
			print "j= "+str(j)
			candidates = []
			# calculate the path to 'j' from 1 given a budget
			# of m edges that are specified in set
			#print "j"+str(j)
			bitmask = calculateBitmask(set);
			# if there is only one element 
			if len(set) == 2: 
				if G[sourceVertex][j]!=None:
					M[bitmask][j] = G[sourceVertex][j]
				else: 
					M[bitmask][j] = INFINITE
			else:
				# candidate set is bigger
				# do brute force search from 1 to k k to j
				for k in set:
					if k==1 or k==j:
						continue
					_set =[i for i in set]
					print "k="+str(k)
					if G[k][j]!=None:
						candidate = calculateSubsetDistance(M,G,_set,j,sourceVertex)
						candidates.append(candidate);

				M[bitmask][j] = min(candidates)  

	#print sets

print M
