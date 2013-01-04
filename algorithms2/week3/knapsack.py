#In this programming problem 
#and the next you'll code up the knapsack algorithm from lecture

import csv as csv


def knapsack(i,size,value,weight,m):
	if m[i][size] != 0: 
		return m[i][size]
	
	wi = weight[i];
	vi = value [i];
	if i==0:
		if wi <size:
			m[0][size] = vi;
			return vi;
		else:
			m[0][size]= 0
			return 0;

	subproblem1 =0
	if wi<= size:
		subproblem1 = vi+knapsack(i-1,size-wi,value,weight,m)
	
	subproblem2= knapsack(i-1,size,value,weight,m)
	
	if subproblem2> subproblem1:
		m[i][size] = subproblem2  
	else: 
		m[i][size] = subproblem1

	return m[i][size]


def iterative(value, weight,m,n,W):
	print "iterating"
	for i in range(1,n+1):
		wi = weight[i-1]
		vi = value[i-1]
		if i<3:
			j =i
			prior = i-1
		else:
			j = (i % 3)
			if j==0:
				prior = 2;
			else:
				prior = j-1
		for w in range(0,W):
			subproblem1 = m[prior][w]
			if w-wi<0:
				subproblem2 = -1000;
			else: 
				subproblem2 = m[prior][w-wi]+vi
		
			if subproblem1 > subproblem2:
				m[j][w] = subproblem1
			else:
				m[j][w] = subproblem2
	
		# free up some memory
		#if (i>=2):
		#	m[i-2] = []

	
	return m[j][W-1]



f = open('./knapsack1Sorted.txt');
reader = csv.reader(f,delimiter=" ",quoting=csv.QUOTE_NONE)

value = [];
weight =[]
W = 10000;
n = 100



#W = 2000000;#knapsack size
#n = 500 ;#total number of items

#W = 10;
#n = 4

# matrix [i,w] maximun -combined- value
# of any subset of items from {1..i} of size 
# ad most w
# of this matrix  m[n,W]
# is our solution
# using list comprehensions in python
# this is initializing the matrix all to 0
# trying to optimize and only keeping three rows
m =  [[0 for w in range(W)] for i in range(3)]

for row in reader:
	value.append(int(row[0]))
	weight.append(int(row[1]))




print "maximum value"
max = iterative(value, weight,m,n,W)
# iterative takes 25 mins but recursive takes even longer

#max = knapsack(n-1,W,value,weight,m)

print max
