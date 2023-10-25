#!/usr/local/bin

"""
events coming from stream

photo upload 

1 - click on browse
2 - select pics
3 - check for any edits
4 - click on upload

For each user that does this action, there are events generated with following info -
user_id | step_num | event_timestamp

order is not guranteed


u1, 1, 2020-05-30 00:00:01
u1, 2, 2020-05-30 00:00:02
u2, 1, 2020-05-30 00:00:02
u3, 1, 2020-05-30 00:00:02
u1, 3, 2020-05-30 00:00:03
streaming solution to calculate average time taken for each step

"""
import datetime
import sys
from datetime import timedelta
from datetime import date
from datetime import datetime
import collections

def main():
    f = open ('./data_bart.txt')
    data = []

    for l in f:
        data.append(l.strip())

    # streaming requires we choose a window for our calculations
    # window should be based on time 
    windows = {}
    # identify windows by their boundaries
    # so key of hash is a tuple

    
    # window size is, say, 10 items
    # for now we do not enforce window size
    WINDOW_SIZE = int(sys.argv[1]) 

    NUMBER_STEPS = 4

    # do we want to be doing date differences 

    # assume fist window 


    window = collections.deque()
    
    events = []

    
    def calculate_avg(window):
        cache = {}
        result = {}
    
        for w in window:
            (user, step, ts) = w
            if cache.get(user) is None:
                cache[user] = [0] * (NUMBER_STEPS + 1) 
            cache[user][int(step)] = ts.timestamp()

        # now we have all data parsed 

        for u in cache.keys():
            
            for i in range(2, NUMBER_STEPS+ 1):
                if result.get(i) is None:
                    result[i] = []
                step = cache[u][i]
                prior = cache[u][i-1]
                if step != 0 and prior != 0:
                    result[i].append(step -prior)

        # this does not have averages but has 
        # the timeseries over which avergaes can be calculated
        
        #print (cache)
        return result


    for event in data:
        event = event.split(',')
        
        (user, step, _time) = (event[0].strip(), event[1].strip(), event[2].strip())
        events.append((user, step, datetime.strptime(_time, "%Y-%m-%d %H:%M:%S")))
    
    # pretending this for loop is our event stream

    # while windows should be time based on stream time
    # we use 10 records for window size

    # persisting here the data we parse out of the window
    
    i = 0 

    while i < (len(events)):
        

        while (len(window)< WINDOW_SIZE):
            window.append(events[i])
            i = i + 1
            
            # do computation
        result = calculate_avg(window)
        print(result)


        # pretend time passes
        # now our window moves forward
        # if it is a disjoined window
        # we would empty it completely
        # we just remove couple elements
        # so windows are not disjointed
        window.popleft()
        window.popleft()
        window.popleft()

        




if __name__=="__main__":
    main()
