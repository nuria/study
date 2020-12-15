#!usr/local/bin/python
f = open ('./input9.txt')


window_length = 25
data = []


def find_two_contiguous(data,total):
	# seems like a Dp candidate 
	# we need to keep track of 1st and last index of sum
	
	# this one 	
	# i is the rows, j columns
	# DP[1][1] = data[1]
	# DP[0][3] = sum(data[0:3 + 1 ])
	#DP[i][j] = sum between i and j numbers
	DP = [[0] * len(data) for i in  range(len(data)) ]


	for i in range(0, len(data)):
		DP[i][i] = data[i]
	for i in range(0, len(data)):
		for k in range(i +1, len(data)):
			if i == 0:
				DP[i][k] = DP[i][k-1] + data[k]
			else:
				DP[i][k] = DP[i-1][k] - data[i-1]
			if DP[i][k] == total:
				return (i, k)

for l in f:
	data.append(int(l))

l = len(data)

s = 0
e = window_length
while (True):
	window = set(data[s:e])
	target = data[e]
	
	print target

	# check
	found  = False
	for w in window:
		# existe a + b = target
		complementary = target - w
		if complementary != w and complementary in window:
			found = True
			break

	if not found:
		print "target not found: {0}".format(target)
		# 90433990
		(n1, n2) = find_two_contiguous(data, target)
		print "the contiguous set starts at  {0} and finish at {1}". format(data[n1], data[n2])
		print min(data[n1:n2]) + max(data[n1:n2])
		exit(1)
	s = s + 1
	if e +1 < l:
		e = e + 1
	else:
		break
	
print" -1"
