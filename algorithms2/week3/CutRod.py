# See page 363 of introduction to algorithms 
# Rod cutting problem, given a rod of 'n' inches and a table of 
# prices pi for i=1,2,3..
# Determine the maximum revenue rn obtainable by
# cuting the rod and selling the pieces
# note that if price pn for a rod of length n is large enough
# an optimal solution might require not cuting at all

P = [] # sample table of prices,it is an array for now
P.append(0);
P.append(1);
P.append(5);
P.append(8);
P.append(9);
P.append(10);
P.append(17);
P.append(17);
P.append(20);
P.append(24);
P.append(30);


# Recursive implementation
# We view a descomposition as consisting
# of a first piece of legth i
# cut off the left hand and then a right hand remainder of n-1
# only the remainder and not the first piece must be further 
# divided
# base case: size i=n P =Pn
# remainder : size 0 with P =0
# P = prices array
def cutRod1(p,n,Q):
	# if we have this value skip computation
	if Q.get(n) >=0:
		return Q[n]

	if n==0:
		q=0
	else: 
		q =-1000
		for i in range(1,n+1):
			maxRevenueSubproblem = p[i]+ cutRod1(p,n-i,Q)
			if (maxRevenueSubproblem> q):
				q = maxRevenueSubproblem
	Q[n] = q
	return q


def cutRod2(p,n):
	Q = {}
	Q[0] = 0
	
	S = {}; # store sizes here
	for j in range(1,n+1):
		q = -1
		for i in range (1,j+1):
			subProblem = p[i]+Q[j-i]
			print " i="+str(i)+"j= "+str(j)+"revenue="+ str(subProblem)	
			if subProblem>q:
				 q = subProblem
				 S[j] = i;
		Q[j] = q
			

	print S 
		
	return Q[n]



# initialize memonization array
# with arbitrary negative values
Q = {}
for i in range(1,10+1):
	Q[i] = -1000;



# now try to compute the solution at each level
maxRevenue = cutRod2(P,10)
print "max revenue"
print maxRevenue
maxRevenue = cutRod1(P,10,Q)
print "max revenue"
print maxRevenue


print cutRod1(P,4,Q);

