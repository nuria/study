#!/usr/local/bin

"""
heap that will have add and pop methods
"""

class Nheap:
    def __init__(self):
        self.h = []
        self.h.append(0)

    def __str__(self):
        return " ".join(map(str, self.h))

    def parent(self,i):
        # given an index in the array figures out index of its parent
        if i ==1:
            # root node
            return None
        else:
            return i/2

    def children(self,i):
        # given an index in the array figures it out indexes of its children
        # it is easier to do it if array starts on 1
        # so we are not going to use its zero item
        # heap only has one element
        if len(self.h) == 2:
            return (None,None)

        if 2*i < len(self.h):
            right_index = 2*i
        else:
            right_index = None

        if 2*i +1 < len(self.h):
            left_index = 2*i+1
        else:
            left_index = None

        return (right_index, left_index)


    def add(self, item):
        # put item on a "leaf" spot, that is at the end of the array
        self.h.append(item)
        # now we need to maintain the heap invariant
        self._bubbleup(len(self.h)-1)

    """
    Make sure that added item maintains the heap invariant
    (it is smaller than any of its children)
    """
    def _bubbleup(self,item_index):
        if item_index == 1:
            return
        parent_index = self.parent(item_index)
        item  = self.h[item_index]

        if item < self.h[parent_index]:
            tmp = self.h[parent_index]
            self.h[parent_index] = item
            self.h[item_index] = parent
        # bubble again just in case
        self._bubbleup(parent_index)

    def pop(self):
        if len(self.h) == 1:
            return None

        if len(self.h) == 2:
            return  self.h.pop()


        top = self.h[1]
        # now put one of the leafs on top of the root
        item = self.h.pop()
        self.h[1] = item
        self._bubbledown(1)
        return top

    # maintain the heap invariant, see if this node needs to be swapped with
    # any of its children
    def _bubbledown(self, item_index):
        # see if it needs to be swap with any of its children
        (right_index, left_index) = self.children(item_index)

        # swap with smallest child
        if right_index is not None and left_index is not None:
            if self.h[item_index] > min(self.h[right_index], self.h[left_index]):
                # swap with smaller child
                if self.h[right_index] > self.h[left_index]:
                    self.swap(item_index, left_index)
                    self._bubbledown(left_index)
                else:
                    self.swap(item_index, right_index)
                    self._bubbledown(right_index)
        else:
            # one of children is missing
            # if both are missing do nothing
            if right_index is not None:
                if self.h[item_index] > self.h[right_index]:
                    self.swap(item_index, right_index)
                    self._bubbledown(right_index)
            elif left_index is not None:
                    self.swap(item_index, left_index)
                    self._bubbledown(left_index)

    # h[j] is less than h[i], value is moving up
    def swap(self, i, j):
        tmp = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = tmp

if __name__ =="__main__":
    nheap =Nheap()
    nheap.add(5)
    nheap.add(7)
    nheap.add(8)
    nheap.add(10)
    nheap.add(56)
    nheap.add(45)

    print str(nheap)
    _min = nheap.pop()
    print _min
    while _min is not None:
        _min = nheap.pop()
        print _min
        print str(nheap)
