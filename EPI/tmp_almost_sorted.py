#!usr/local/bin
import heapq

def almost_sorted(A, k):

    A_s = []
    # we know every element is ad most k positions from its rightful one
    # can we keep a heap of size k to help with lookups?
    h = []
    heapq.heapify(h)


    for a in A:
        if len(h) <= k+1:
            heapq.heappush(h, a)
        else:
            A_s.append(heapq.heappop(h))
            heapq.heappush(h,a)

    # empty heap
    while len(h) > 0:
        A_s.append(heapq.heappop(h))

    return A_s



if __name__=="__main__":

    A= [3,-1, 2,6, 4, 5, 8]
    # ad most k away from its current position
    # k == 2 in prior example
    print almost_sorted(A, 2)
