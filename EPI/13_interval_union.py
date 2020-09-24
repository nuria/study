#!/usr/local/bin/python

class Interval:

    def __init__(self , s, e):
        self.s = s
        self.e = e


    def __repr__(self):
        return "[ "  + str(self.s) +"-"+ str(self.e)+"]"

class Point:
    def __init__(self, x, qualifier):
        self.x = x
        self.qualifier = qualifier

    def __repr__(self):
        return "(" + str(self.x) + str(self.qualifier) + ")"

def join_intervals(l):
    # transform the list of intervals into a list of points
    # so we know which one is start and which one is end
    l = map(lambda x: (Point(x.s, 's'), Point(x.e, 'e')),l)

    l = [item for sublist in l for item in sublist]

    print "unsorted"
    print l

    print "sorted"
    l.sort(key=lambda p:p.x)
    print l

    intervals = []
    counter = 0
    start = None
    for item in l:
        # keep track of starts and ends
        if item.qualifier == 's':
            counter += 1
            if start is None:
                start = item
        else:
            counter -= 1

        if counter==0:
            intervals.append((start, item))
            start = None

    return intervals



if __name__=="__main__":
    I1 = Interval(1,1)
    I2 = Interval(2,4)
    I3 =  Interval(3,4)
    I4 = Interval(0,3)
    I5 = Interval(5,7)

    l = [I1, I2,I3, I4, I5]
    # sort earliest start time
    l.sort(key=lambda x:x.s)

    print l
    print join_intervals(l)
