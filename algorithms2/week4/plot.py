
# plot graph with networkx
# http://networkx.lanl.gov/tutorial/tutorial.html#graph-generators-and-graph-operations
import csv as csv;
import networkx as nx;
import matplotlib.pyplot as plt


#----------------------------  main program ---------------------

#f = open('./g3.txt','rb');
f = open('./testCase7.txt','rb');
reader = csv.reader(f,delimiter=' ',quoting=csv.QUOTE_NONE); 


firstRow = reader.next();

v = int(firstRow[0]);#number of vertexes
e = int(firstRow[1]); #number of edges

DG=nx.DiGraph()
for row in reader:
	#build adjacency list,keeping pointers like:
	#tail ---->head
	tail = int(row[0])
	head = int(row[1])
	w = int(row[2])
	DG.add_weighted_edges_from([(tail,head,w)])


# Graph is now stored in G

pos = nx.shell_layout(DG)
nx.draw(DG,pos,node_color='#A0CBE2',edge_color='#BB0000',width=2,edge_cmap=plt.cm.Blues,with_labels=True)
plt.show()
#plt.savefig("graph.png", dpi=500, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1) 
