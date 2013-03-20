# The goal of this problem is to implement 
# the 'Median Maintenance' algorithm (covered in the Week 5 lecture on heap applications
# The text file contains a list of the integers from 1 to 10000 in unsorted order
# you should treat this as a stream of numbers, arriving one by one. 
# Letting xi denote the ith number of the file, 
# the kth median mk is defined as the median of the numbers x1,.,xk. 
#(So, if k is odd, then mk is ((k+1)/2)th smallest 
#number among x1,...,xk; if k is even, then mk is the (k/2)th smallest number among x1,...,xk.)

import heapdict as hpdict

# negating entries to support extract max with a min heap
class MaxHeap:
	def __init__(self):
		self.heap = hpdict.heapdict()
	def add(self,item):
		priority = item*(-1)
		self.heap[item] = priority
	def remove(self,item):
		del self.heap[item]
	def peekitem(self):
		return self.heap.peekitem()[0]
	def popitem(self):
		return self.heap.popitem()[0]
	def getHeap(self):
		return self.heap
	def getLen(self):
		return len(self.heap)

def heapToString(h):
	msg =" heap {"
	for i in h.keys():
		msg = msg +" "+str(i)+" :"+str(h[i])
	return msg+"}"



f = open('./Median.txt','r');
#f = open('./testCase4.txt');
D = [] ; #data array , holds the whole dataset

# we will negate values to insert them and 'un-negate' them to compare
# as python only supports min heap
lowHeap = MaxHeap(); #supports extract MAX
highHeap =hpdict.heapdict(); #supports extract MIN

for line in f:
	D.append(int(line));


maxLowHeap = None;
minLowHeap = None;

k = 0
sumMedian = 0;

for x in D:
	k = k+1
	# we need to initialize those
	if lowHeap.getLen()==0:
		lowHeap.add(x)
		sumMedian = x;
		continue;
	elif len(highHeap) ==0:
		# see where does the second entry fit
		prior = lowHeap.peekitem()
		if x>prior:
			#insert into high heap
			highHeap[x] = x;
			sumMedian = sumMedian*2; #we know is the same median than before
		else:
		   #insert into low heap
		   lowHeap.remove(prior)
		   lowHeap.add(x)
		   highHeap[prior]=prior
		   sumMedian = sumMedian+x
		continue;

	maxLowHeap = lowHeap.peekitem()
	minHighHeap = highHeap.peekitem()[0]


	if x < maxLowHeap:
		#insert in low heap
		lowHeap.add(x);
		lowHeap.remove(maxLowHeap)
		highHeap[maxLowHeap] = maxLowHeap
	elif x> minHighHeap:
		highHeap[x] =x
		del highHeap[minHighHeap]
		lowHeap.add(minHighHeap)
	else :
		# x could be inserted in either heap
		# let's actually insert it on the high heap
		highHeap[x] = x
	
	# rebalance
	lLow =lowHeap.getLen()
	lHigh = len(highHeap)
	# the way we are doing it we cannot be off for more than one
	if lLow>lHigh+1:
		#move from low to high
		maxLowHeap = lowHeap.popitem();
		highHeap[maxLowHeap] = maxLowHeap
	elif lHigh>lLow+1:
		#move from high to low
		minHighHeap = highHeap.popitem()[0];
		lowHeap.add(minHighHeap)

	#recalculate lengths
	lLow =lowHeap.getLen()
	lHigh = len(highHeap)


	if k % 2 ==0:
		half = int(k/2)
	else: 
		half = int((k+1)/2)
	
	#print "k"+str(k)
	#print "m="+str(half)
	#print "x"+str(x)

	#print "low heap"
	#print heapToString(lowHeap.getHeap())
	#print "high heap"
	#print heapToString(highHeap)

	#print "median"
	if half>lLow:
		#print "from high heap "+str(highHeap.peekitem()[0])
		sumMedian = sumMedian +highHeap.peekitem()[0];
	else :
		#print "from low heap " +str(lowHeap.peekitem());
		sumMedian = sumMedian+ lowHeap.peekitem();
	#print "----sum median"+str(sumMedian)

# done with heaping, print heaps

print "low heap"
#print heapToString(lowHeap.getHeap())

print "high heap"
#print heapToString(highHeap)

print "sum median for "+str(k)+" items"
print sumMedian
