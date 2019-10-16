#!/usr/local/bin/python
# for a stream of N items calculates the median
# media is item x[N/2] (even) or x[N+1/2] (odd)

# solution is the sum of these N medians, modulo N
# note that  we are treating  the stream of numbers as real time
# so we are computing a median EVERYTIME we ngest a number
# and computing at the end the sum of all those medians
# the name median makes sense if you do not think is the median of the full set


import heapq as h
import sys


class Heap():
    def __init__(self, maxHeap=False):
        self.heap = []
        self.maxHeap =  maxHeap

    def addItem(self,item):
        # negating items so largest would be at root (with wrong sign)
        if self.maxHeap is True:
            h.heappush(self.heap, item *(-1))
        else:
            h.heappush(self.heap, item)

    def getRootItem(self):
        if len(self.heap) == 0:
            return None
        item = h.heappop(self.heap)
        if self.maxHeap :
            item = item * (-1)
        return item

    def peekRootItem(self):
        if len(self.heap) == 0:
            return None
        item = min(self.heap)
        if self.maxHeap :
            item = item * (-1)
        return item

    # TODO improve , this can be o(1)
    def getSize(self):
        return len(self.heap)

    def toString(self):
        return self.heap

def main():
    medians = []

    f = open(sys.argv[1])
    # this is a max heap, max is root
    heap_low = Heap(True)
    # this is a min heap, min is root
    heap_high = Heap()

    for l in f:
        item = int(l.strip())

        if heap_low.getSize() == 0:
            heap_low.addItem(item)
        # if there are 13 items, heap low needs to have 7
        # if the k median of an odd number is (k+1)/2
        # for an even number is k/2
        elif item < heap_low.peekRootItem():
            heap_low.addItem(item)
            # adjust and rebalance
            if heap_low.getSize()  -heap_high.getSize() >1:
                heap_high.addItem(heap_low.getRootItem())
        else:
            heap_high.addItem(item)
            if heap_high.getSize() > heap_low.getSize():
                heap_low.addItem(heap_high.getRootItem())

        medians.append(heap_low.peekRootItem())

        #print heap_low.toString()
        #print heap_high.toString()


    # now get k item
    size1 = heap_low.getSize()
    size2 = heap_high.getSize()
    print "first heap {0} elements, second heap {1} elements".format(size1, size2)

    N  = len(medians)
    #print medians
    # this thing of calling "median" the sum is a bit strange
    median = reduce(lambda x,y: x+y, medians)

    print median

    print (median % N)

if  __name__=='__main__':
    main()




