# traveling salesman problem 
#  The first line indicates the number of cities. Each city is a point in the
#  plane, and each subsequent line indicates the x- and y-coordinates of a
#  single city.
# The distance between two cities is defined as the Euclidean distance 
#import numpypy
import csv as csv
import math as math
import itertools;
#import numpy

# calculates the euclidean distance
def calculateDistance(x0,y0,x1,y1):
	d = (x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)
	d = math.sqrt(d)
	#rouding distances to nearest integer
	return d


################################ main program ###################

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


# let's print solutions, crappy local search
# but solution has to be close to the one i got with 20 points

'''
sol1 =[1,2,6,10,11,12,15,19,22,23,21,20,25,24,16,17,18,14,13,9,7,3,4,8,5,1]
tour1 = 0
s1= sorted(sol1)
print s1
sol2=[1,2,6,10,11,12,15,14,16,24,25,20,21,23,22,19,18,17,13,9,7,3,4,8,5,1]
tour2 = 0
s2= sorted(sol2)
print s2

sol3=[1,2,6,10,11,12,15,19,18,22,23,21,17,20,25,24,16,14,13,9,7,3,4,8,5,1]
tour3 = 0
s3 = sorted(sol3)
print s3

sol4=[1,2,6,10,11,12,15,19,18,22,23,21,17,20,25,24,16,14,13,9,7,3,4,8,5,1]
tour4 = 0
s4 = sorted(sol4)
print s4




for i in range(0,len(sol1)+1):
	if i <len(sol1)-1:
		node1 = sol1[i]
		next1 = sol1[i+1]
		print str(node1)+"->"+str(next1)
		tour1 = tour1 +G[node1][next1]
		node2 = sol2[i]
		next2 = sol2[i+1]
		tour2 = tour2+G[node2][next2]
		node3 = sol3[i]
		next3 = sol3[i+1]
		tour3 = tour3+G[node3][next3]
		node4 = sol4[i]
		next4 = sol4[i+1]
		tour4 = tour4+G[node4][next4]




print tour1
print tour2
print tour3
print tour4
'''


