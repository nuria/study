#!/usr/local/bin

import collections 

def main():

    events = []
    f = open('./data_streaming.txt')
    for l in f:
        l = l.strip()
        (machine, process, state, ts) = l.split()
        events.append((machine, process, state, float(ts)))

    START = "start"
    END = "end"

    def window_duration(events):
        
        # stores processes and durations
        d = {}
        h = {}
        for e in events:
           
            print (h)
            
            (machine, process, state, ts) = e
            key = machine + process
            
            if d.get(process) is None:
                d[process] = []

            if state == START:
                # append to queue , FIFO
                if h.get(key) is None:
                    h[key] = collections.deque()
                (h[key]).append(ts)
            else:
                # compute diference, pop from queue 
                # does not account for late arriving data 
                
                if h.get(key) is None:
                    continue
                else:
                    q = h[key]
                    start = q.popleft() 
                    if ts > start:
                        d[process].append(ts-start)
        return d



    # first sort by time
    #(machine, process, state, ts)

    events.sort(key=lambda x: x[3])
    #print(events)

    WINDOW_SIZE = 10
    

    averages = {}

    event_window = collections.deque()

    # we are going to compute an average 
    
    i = 0
    while i < len(events):
        # put data into window
        while len(event_window) <= WINDOW_SIZE:
            e = events[i]
            event_window.append(e)
            i = i + 1
            # now compute with events we have
        # recomputes everytime
        d = window_duration(event_window)
        
        max_avg_duration = 0
        max_process = None

        for k in d.keys():
            diff = d[k] 
            if len(diff) <1:
                continue
            avg = sum(diff)/len(diff)
            if avg > max_avg_duration:
                max_avg_duration= avg
                max_process = k

        print (" {0} {1}".format(max_process, max_avg_duration))
        
        # we can move window forward by however many 
        # this moves it by 10

        if len(event_window) > 0:
            event_window = []
        i = i + 1

    

        





if __name__=="__main__":
    main()
