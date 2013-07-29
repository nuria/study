#!/usr/bin/python
import sys

# size of the matrix
# execute like 
# time python mutiply.py 2
# with regular python takes 16 secs to mutiply matrix of 300 elements
# with pypy it takes about 1 sec
# for 500 elements it takes about 5 sec
#


size = int(sys.argv[1]);


print "matrix size = "+str(size);

# define matrixes, start indexing at '1'
a1 = [ [1 for row in range(0,size)] for i in range(0,size)]
a2 = [ [1 for row in range(0,size)] for i in range(0,size)]
b = [[0 for row in range(0,size)] for i in range(0,size)]



#print a1
#print a2

for i in range(0,size):
	for j in range(0,size):
		tmp = 0
		for r in range(0,size):
			tmp = a1[j][r]*a2[r][j] + tmp
		b[i][j] = tmp

#for r in range(0,size):
	#print b[r]
