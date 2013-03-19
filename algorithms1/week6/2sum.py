#find two distinct numbers that add to  athird number 
#actually to  a third set of numbers [2500,4000]

# given a sum target returns true if
# it can be achieved with two numbers
# of the set
def _2sum(S,target):
	for item in S:
		s = target-item
		if item > target or s==item:
			continue;
		elif s in S:
			return True;
	return False; 


f = open('./2SUM.txt','r');
S = set();

for line in f:
	line = int(line);
	if line >4000:
		continue;
	S.add( line)


T = set();
for target in range(2500,4001):
	if _2sum(S,target):
		T.add(target)

print T
print len(T)
