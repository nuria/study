#Points should be an iterable of pairs e.g. [(x1,y1), (x2, y2)...] and path and iterable with the order e.g. (1,4,2,0,1). 
#If you call it without a path it will draw only the points.

import pylab
import csv
def draw_path(points, path=()):
  n = len(points)
  data = pylab.array(points)    
  labels = ['{0}'.format(i) for i in range(n)]

  if path:
    data2 = data[pylab.array(path)]
    pylab.plot(data2[:, 0], data2[:, 1], marker = 'o', c = 'r')
  else:
    pylab.scatter(data[:, 0], data[:, 1], marker = 'o', c = 'r')

  for label, x, y in zip(labels, data[:, 0], data[:, 1]):
    pylab.annotate(label, xy = (x, y))    

  pylab.show()



f = open ('./cities.txt');
reader = csv.reader(f , delimiter=' ',quoting=csv.QUOTE_NONE);

firstRow = reader.next();

v = int(firstRow[0]); # number of vertexes

P = [] # stores x, y for each city
# we shall precalculate distances from anyone to anyone so each vertex will have
# 24 edges...
i = 0;

S = {} # set cache, see if it improves performance
B = {} # bitmask cache
INFINITY = 1000000;

for row in reader:
	P.append((float(row[0]),float(row[1])))


draw_path(P);
