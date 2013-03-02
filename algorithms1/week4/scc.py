# large graph 
# compute strongly connected components
# input format is tail--->head
# vertexes are just labels
# This program will retun the size of 5 biggest SCC, like 3,3,3,0,0
# if there are 3 SCC with 3 nodes plus no more
import csv as csv

#depth first search,returns the explored set
def DFS(Q,node):
	E = set() ;#explored set
	# The list methods make it very easy to use a list as a stack, 
	# where the last element added is the first element retrieved LIFO
	# To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. 
	stack = []
	stack.append(node)
	while len(stack) >0:
		E.add(node)
		#print "exploring " + str(node);
		#print Q[node]
		for v in Q[node]:
			#print v
			if not (v in E):
				stack.append(v);#appends to the front
		node = stack.pop() #pops from the front

	return E



	


#f = open('testCase1.txt');
f = open('./scc.txt');
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


sourceVertex = 1
E = DFS(G,sourceVertex);
print " From source vertex " + str(sourceVertex)
print " We found "+str(len(E))+" nodes";

