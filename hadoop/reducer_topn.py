#!/usr/bin/python
import sys
import heapq as heapq

# reads line like key, value pairs
# and picks up the ten items with highest value

# min heap, since we are looking for max values we
# store negative values
h =[]
for line in sys.stdin:
    items = line.strip().split("\t");
    key = items[0];
    value = int(items[1]) *(-1)


    heapq.heappush(h,(value,key))

# now retrieve the top ten items
# and spit them out in key, value format
for i in range(0,10):
    value,key = heapq.heappop(h);

    value = value*(-1)
    print "{0}\t{1}".format(key,value)
