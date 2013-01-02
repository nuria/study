#In this programming problem 
#and the next you'll code up the knapsack algorithm from lecture

import csv as csv



f = open('./knapsack1.txt');
reader = csv.reader(f,delimiter=" ",quoting=csv.QUOTE_NONE)

value = [];
weight =[]
W = 10000;
n =100
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
m =  [[0 for i in range(W+1)] for j in range(n+1)]

for row in reader:
	value.append(int(row[0]))
	weight.append(int(row[1]))



for i in range(1,n+1):
	wi = weight[i-1]
	vi = value[i-1]

	for w in range(1,W+1):
		subproblem1 = m[i-1][w]
		if w-wi<0:
			subproblem2 = -1000;
		else: 
			subproblem2 = m[i-1][w-wi]+vi
		
		if subproblem1 > subproblem2:
			m[i][w] = subproblem1
		else:
			m[i][w] = subproblem2
	
	# free up some memory
	if (i>=2):
		m[i-2] = []

print "maximum value"
print m[n][W]


