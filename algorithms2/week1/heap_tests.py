import heapq as hp
import pprint

def heapsort(iterable):
	'Equivalent to sorted(iterable)'
	h = []
	for value in iterable:
		hp.heappush(h, value)
	return [hp.heappop(h) for i in range(len(h))]
	


s=[]
s= heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

for entry in s:
	print entry


initial = [(1,'task 1') , (3,'task 3'), (5,'task 5'), (7,'task 7'), (9,'task 9'), (2,'task 2'), (4,'task 4'), (6,'task 6'), (8,'task 8') ,(0,'task 0')]
initial = heapsort(initial);

for entry in initial:
	print initial

