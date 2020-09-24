#!usr/local/bin

# returns a set with best visisting times
import heapdict

def best_visiting_times(I):
    # focus en end times
    h = heapdict.heapdict()
    for i in I:
        # interval is the key
        # end of interval is the value inserted on
        # the heap
        h[(i[0], i[1])] = i[1]


    result =[]

    while (len(h) >0):
        # this is the smallest end time
        (interval, end)  = h.popitem()

        # now see how many task are 'happening' or 'finishing'
        # at that time
        result.append(end)
        for i in I:
            if i[0] <= end and i[1] >= end:
                if h.get((i[0],i[1])):
                    h.pop((i[0],i[1]))

    return result

if __name__=="__main__":
    I = [[0,3], [2,6],[3,4],[6,9]]
    I  = [[1,2], [2,3], [3,4],[2,3],[3,4],[4,5]]
    print best_visiting_times(I)

