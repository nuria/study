#quicksort
# this implementation chooses as pivot the 1st element

# partition arround a pivot
def partition(a):
	p = a[0];
	# keeps track of <p elements
	i =0
	# keeps track of the elements we have seen
	j = 0
	
	for j in range(1,len(a)):
		element = a[j]
		if a[j]<=p:
			current = a[j]
			firstBig = a[i+1]
			a[j] = firstBig
			a[i+1] = current
			i = i+1;
	#swap pivit with a[i-1]
	a[0] = a[i]
	a[i] = p
	
	# we return the index that splits the <p 
	# part of the array
	return i,a	

def quicksort(a):
	i,a = partition(a);

	#print "semi sorted array"
	#print a
	#print "the boundary is"+str(i)

	left = a[0:i+1];
	if len (left) > 1:
		left = quicksort(left) # will get indexes 0 to i
	
	right = a[i+1:len(a)];
	if len(right) > 1:
		right  = quicksort(right);

	result = left+right
	return result


file = open ('./testCase1.txt');
#file = open('./QuickSort.txt');
A = [];
for line in file:
	A.append(int(line));


s = quicksort(A);

print "sorted"
print s

