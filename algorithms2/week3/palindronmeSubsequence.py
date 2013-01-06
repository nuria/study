#Given a sequence, find the length of the longest palindromic 
#subsequence in it. For example,if the given sequence is BBABCBCAB, 
#then the output should be 7 as BABCBAB is the longest palindromic subseuqnce in it. 
#BBBBB and BBCBB are also palindromic subsequences of the given sequence, 
#but not the longest ones.

from optparse import OptionParser

parser = OptionParser()
(options, args) = parser.parse_args()

input = args[0];
input  = list(input) 

# the longes palidrome subsequence of a string
# is the longest common subsequence between a string and its reverse

def LCSLength(x, y):
	lenx =len(x)
	leny = len(y)
   	m =  [[0 for w in range(lenx)] for i in range(leny)] 
	for i in range(0,lenx):
		m[i][0] = 0
	for j in range(0,leny):
		m[0][j] = 0
	
	for i in range(1,lenx):
		for j in range(1,leny):
 			if x[i] == y[j]:
				m[i][j] = m[i-1][j-1] + 1
			else:
				subproblem1 = m[i][j-1];
				subproblem2 = m[i-1][j];
				if subproblem1>subproblem2:
					m[i][j]  = subproblem1;
				else:
					m[i][j] = subproblem2;
	return m[lenx-1][leny-1]




r = []
l =len(input)
for i in range(len(input)):
	r.append(input[l-1-i]);
result = LCSLength(input,r);
print result;
