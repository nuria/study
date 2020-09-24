#!usr/local/bin/python
import heapq

# this would be a min heap so smallest item
# is at top so we need to enter (string ,len)  pairs
# if it was a heapdict
# since it is a heap then we just enter length
items = heapq.heapify(list())

# number of items to keep
K =  10


def ingest(text):
    if len(items) > K:
        # see if we need to expell the smallest
        (l, s) = items[0]
        if l < len(text):
            heappop(items)
            heappush((len(text), text))
    else:
        heappush(len(text), text)


    # look at top of heap


if __name__=="__main__":



