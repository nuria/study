
# file with 1000 entries
# weight, length
# write algorithm that schedules jobs in decreasing order of (wi-li)
# to break ties, job with higher weight goes first

# report the sum of weighted completition times

import csv as csv
import heapq as hp



class Task(object):
	def __init__(self, weight, length): 
		self.weight = weight
		self.length = length
		self.cost = weight-length
		self.ct = 0; #completition times
	def __cmp__(self, obj): 
		if self.cost != obj.cost:
			# std compare for lengths, lower lengths go 1st
			# i.e. decreasing value of w-l
	   		return cmp( obj.cost,self.cost)
		else: 
			# if cost is same actually higher weights go first
			return cmp(obj.weight,self.weight)
	def __repr__(self):
		return '{w:'+str(self.weight)+',l:'+str(self.length)+'}'



h = [] ; #heap where we will keep the sorted stuff

f  = open('./jobs_small.txt', "rb")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

for row in reader: 
	w = float(row[0])
	l = float(row[1])
	hp.heappush(h, Task(w,l))


# print heap
sortedTaskList = [hp.heappop(h) for i in range(len(h))]


# go through list storing completition times per each Task
timeElapsed = 0
weightedCT = 0  #weighted sum of completition times

for task in sortedTaskList:
	timeElapsed = timeElapsed+task.length
	task.ct = timeElapsed
	print task
	weightedCT = weightedCT + task.weight* task.ct 



print "total time" +str(timeElapsed)
print "weighted completition times: "+str(weightedCT) 




