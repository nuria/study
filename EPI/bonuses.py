#!/usr/local/bin
import sys
import heapq as hp

def main():
    # consider iteratively updating the assigment
    work = [300,400,200,500]
    r =[1] *len(work)

    #work = [300,400,400,400]

    # stores index of processed items
    processed = [False] *len(work)
    # we start by the one who is least productive, we need a min heap
    h = [] # values are (w, index)
    
    for i in range(0,len(work)):
        hp.heappush(h, (work[i], i))

    # the least productive developer does not need more than a single ticket
    (w,index) = hp.heappop(h)
    
    processed[index] = True
    
    while len(h) > 0:
        (w, index) = hp.heappop(h)
        # all devs are initialized to 1        
        
        # this is the next least productive developer
        # does it make more than his neighbourghs
        # if they are processed we know he makes equal or less
        if index > 0:
            if  processed[index-1] and work[index-1] != w:
                # the one to the left makes less
                r[index]  = r[index-1] +1 

        if index < len(work)-1:
            if processed[index+1] and work[index+1] != w :
                #the one to the right makes less
                if r[index] <= r[index+1]:
                    r[index] = r[index+1] + 1 

        processed[index] = True
        print "work:{0}, result:{1}, processed: {2}".format(w,r, processed)

    print work
    print r


if __name__=="__main__":
    main()
