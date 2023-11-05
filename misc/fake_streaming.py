#!/usr/local/lib

import collections


def compute(w):
    # machine, process, state, time
    # we have to group data per process 
    # as it arrives 
    cache = {}
    result = {}

    # cache['p1'] = {start:[], end:[]}
    # this is a possible structure 
    # does not use data per machine
    
    # at the end of processing window events we will have a start-end times per process

    for e in w:
        (machine, p, status, ts) = e
        if cache.get(p) is None:
            cache[p] = {}
            cache[p]['start']= []
            cache[p]['end'] =[]
        cache[p][status].append(ts)

    print (">>>>> window  data ")

    print (cache)


    for p in cache.keys():
        tally = 0
        # now process data per process
        start_ts = cache[p]['start']
        end_ts = cache[p]['end']

        j = 0
        i = 0
        n = 0
        while i < min(len(start_ts), len(end_ts) ) and j < min(len(start_ts), len(end_ts)) :
            # exit if we run out of data to process

            # possible approaches
            # this will depend on data shape
            # is the 1st start before first end? if not 
            # we need to move with different pointers in each list
            # do we order the timeseries? 
            # we decide not to order
            if start_ts[j] < end_ts[i]:
                tally = tally + end_ts[i] - start_ts[j]
                j = j + 1
                n =+ 1
            else:
                while(star_ts[j] > end_ts[i] and j < len(start_ts)):
                    j = j +  1
                if j < len(start_ts):
                    tally = tally + end_ts[i]- start_ts[j]
                    n+=1 

            i = i +1

            result[p] = tally/n

    return result



def main():
    f = open('./data_streaming.txt')
    # calculate avg time per process

    stream = []

    for l in f:
        # machine, process, status, time
        l = l.strip()
        (machine, process, status, time) = l.split()
        stream.append([machine, process, status, float(time)])



    # important is to process just s a window of events
    # we would do this by time , say 5 minutes
    # faking here with number of events

    WINDOW_SIZE = 10

    # we assume windows overlap so we have windows of 10 values 
    # that are set every 5 values
    
    result = []

    w = collections.deque()
    i = 0 
    while i < len(stream):
        while(len(w)< WINDOW_SIZE and i <len(stream)):
            w.append(stream[i])
            i = i + 1
        # process events
        print(w)
        result = compute(w)   
        print(">>results")
        print(result)
        # once process 
        while (len(w) > 5):
            w.popleft()



if __name__=="__main__":
    main()
