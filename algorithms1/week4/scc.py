# large graph 
# compute strongly connected components
# input format is tail--->head
# vertexes are just labels
# This program will retun the size of 5 biggest SCC, like 3,3,3,0,0
# if there are 3 SCC with 3 nodes plus no more
import csv as csv

# depth first search,returns the explored set
# Q is the graph
# l leader for cluster,only relevant on step 2
def DFS(Q,node,calculateTimes,leader=None):
	global t
	# The list methods make it very easy to use a list as a stack, 
	# where the last element added is the first element retrieved LIFO
	# To add an item to the top of the stack, use append(). 
	# To retrieve an item from the top of the stack, use pop() without an explicit index. 
	stack = []
	stack.append(node)
	while len(stack) >0:
		unexploredChildren = False;
		node = stack.pop();
		if (leader!=None) and (node not in L[leader]):
			# using a set as we might pass through
			# here witha node more than once
			L[leader].add(node);
		
		E.add(node)
		#print "exploring " + str(node);
		#print Q[node]
		for v in Q[node]:
			#print v
			if not (v in E):
				#print "adding "+str(v)+" to stack"
				# append 1 at the time otherwise is not depth first search
				# we need to calculate finishing times,thus do not remove base
				# node from stack until all its children have been removed
				stack.append(node);
				stack.append(v);#appends to the front
				unexploredChildren = True;
				break;

		if not unexploredChildren and calculateTimes:
			t = t+1;
			F[t] = node 
			#print "finished exploring " +str(node)
		#print stack

################################ main program ######################

f = open('testCase3.txt');
#f = open('./scc.txt');
reader = csv.reader(f,delimiter=' ', quoting=csv.QUOTE_NONE)


G = {}
GR = {}

for row in reader:
	# there are some white spaces on the graph
	# we will be creating directed and reverse graphs at the same time
	# tail ---> head
	tail = int(row[0]);
	head = int(row[1]);

	if G.get(tail)==None:
		G[tail] =  []
		GR[tail] = []
	if G.get(head) == None:
		G[head]  = [];
		GR[head] = [];

	G[tail].append(head);
	GR[head].append(tail);



# remember we start at the bigest vertex
sourceVertex = max(G.keys());

#finishing times,stored like:  F[time] = node
F={}

# keeping track of explored
E = set() 

# global variable for finished times
t = 0; 


# step 1, run DFS in the reverse graph for all nodes
# calculating finishing times
for vertex in range(sourceVertex,1,-1):
	# DFS updates the explored set (global) and finished times (global)
	if vertex not in E:
		DFS(GR,vertex,True);
		print " From source vertex " + str(vertex)
		print " We found "+str(len(E))+" nodes";



# step 2, run DFS in decreasing order of finishing times
# calculating leaders

# reversing F to print so F[node] = time
#FR = dict (zip(F.values(),F.keys()))
#print "Times per node:"
#print FR

# storing cluster leaders and nodes for debugging puposes
# remove if time takes too much
L = {} 

maxTime = max(F.keys());
E = set();
for t in range(maxTime,1,-1):
	# explore and choose leaders
	vertex = F[t]
	#print "exploring vertex "+str(vertex)
	if vertex not in E:
		leader = vertex
		L[leader] = set()
		DFS(G,vertex,False,leader)
		#substitute by length of set
		L[leader] = len(L[leader])	

#print "Leaders per node"
#print L

# answer is the size of the 5 largest SCCs
# post process

size = L.values()
size.sort(reverse=True);
print size
	


