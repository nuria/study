# compute the number of inversions in the given file
# where the ith row of the file indicates the ith entry of an array
#  merge sort counting how many times do we move elements arround?



def  mergeSort(m):
	l = len(m)

	if l == 1:
		R = m
		return R

	elif l % 2 == 0:
		middle =l/2
	else: 
		middle=(l+1)/2

	#correct by one, length starts at 0
	end_r = middle-1
	left= m[0:middle]
	right = m[middle:l]
	#print "merge sort"
	#print m
	#print right
	#print left

	R = merge(mergeSort(left),mergeSort(right))

	return R

# r = right array
# l= left array
def merge(left,right):
	#print "merge"
	j =0
	i =0
	n = len(right)+len(left)
	R =[]
	for k in range(0,n):
		if i >= len(right):
			# use all 'j' items left
			R.extend(left[j:len(left)]);
			break
		elif j>=len(left):
			# use all 'i' items
			R.extend(right[i:len(right)])
			break
			
		if right[i] < left[j]:
			R.append(right[i]);
			i = i+1
		elif right[i] > left[j]:
			R.append(left[j]);
			j = j+1
		else:
			#equal
			R.append(right[i]);
			R.append(left[j]);
			i=i+1;
			j=j+1;

	return R

		

#f = open('./testCase1.txt');
f = open('./IntegerArray.txt');
data = []
for line in f:
	line = int(line)
	data.append(line)


#we have all data there, how do we calculate inversions?
# merge sort with a counter?

R = mergeSort(data)

print R


