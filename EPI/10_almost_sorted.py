#!usr/local/bin

# long sequence of numbers  and prints them in sorted order, each number is about 'k'
# away from its corrently sorted position
# (3, -1, 2, 6, 4, 5,8) no number is more than 2 away for its sorted position

import heapq

def almost_sorted(a, k):
    result = []
    # first element is ad most k positons away
    # so enter the first k elements

    _heap = []
    for i in range(0, k+1):
        heapq.heappush(_heap, a[i])

    i = k +1

    result.append(heapq.heappop(_heap))

    while i < len(a):
        heapq.heappush(_heap, a[i])
        i = i +1
        result.append(heapq.heappop(_heap))

    for j in range(0, len(_heap)):
        result.append(heapq.heappop(_heap))

    return result

if __name__ == "__main__":

    print almost_sorted([3,-1, 2, 6, 4, 5, 8],2)


