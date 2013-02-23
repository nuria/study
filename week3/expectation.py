# Random variable: Two dice, sum of the rollup
# what is the expectation? weighted average of all possible outcomes

e = 0

for i in range(1,7):
	for j in range (1,7):
		#funny integer division in python,need to cast one to a float
		#print "i="+str(i)+ ", j="+str(j)
		e = e +float((i+j))/36

print "the expectation"
print e
