
# plot graph with networkx
# http://networkx.lanl.gov/tutorial/tutorial.html#graph-generators-and-graph-operations
import csv as csv;
import networkx as nx;
import matplotlib.pyplot as plt


#----------------------------  main program ---------------------

f = open('./smallSet.txt','rb');
reader = csv.reader(f,delimiter='\t', quoting=csv.QUOTE_NONE)


DG=nx.DiGraph()

G = {}
V = 0
for row in reader:
	V = V+1
	v = int(row[0])
	l = len(row)
	for i in range(1,l):
		w = row[i]
		if w.isdigit():
			w = int(w)
		DG.add_weighted_edges_from([(v,w,1)])




# Graph is now stored in G

pos = nx.shell_layout(DG)
nx.draw(DG,pos,node_color='#A0CBE2',edge_color='#BB0000',width=2,edge_cmap=plt.cm.Blues,with_labels=True)
plt.show()

