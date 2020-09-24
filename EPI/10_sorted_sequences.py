#!usr/local/bin
import unittest
import heapq

# merge a set of sorted lists
def merge_sorted(l):
    # using a heap to keep track of items in sorted order
    # seems the way to go
    # EASY:
    # ingest all items and let heap order them given its inner structure
    # kind of feels like cheating and it does not
    # take advange of list being partially sorted
    # o(nlogn)
    # let's use the fact that lists are sorted to keep a tree of ad most h height
    result = []
    # o(n) pass
    cardinal = sum(map(lambda x: len(x), l))
    index = 0
    _heap = []

    # how to loop through the very fist item of each list
    # build 3 iterators
    # remember StopIteration exception
    iterators = map(iter, l)
    index = 0

    while len(result) < cardinal:
        for k in range(0, len(iterators)):
            try:
                item = next(iterators[k])
                heapq.heappush(_heap, item)
            except StopIteration:
                # it is fine, this would happen with a list of lists of different sizes
                pass

        # now we can start moving things to the result array
        result.append( heapq.heappop(_heap))

    return result



class testing(unittest.TestCase):

    def test_happy_case(self):
        s = merge_sorted([[3,5,7], [0,6],[0,6,28]])
        # s should be [0,3,5,6, 6,7,28]
        print s
        self.assertEqual(s, [0,0,3,5,6,6,7,28])

if __name__== "__main__":

    unittest.main().result

