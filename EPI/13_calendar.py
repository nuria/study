#!usr/local/bin

# calendar
# events have : start, finish times
# y cordinate has a spacifiled L (how long the day is)
# each rectangle has teh same height
# the task is to compute the maximun height an event rectangle can have (within the bounds of L?)
# rather: take a number of events (start, end) and determine within the time bounds the maximun numbers
# of events that take place concurrently

class Interval():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[" + str(self.start) + "-"  + str(self.end) + "]"

class Endpoint():
    def __init__(self, digit, qualifier):
        # qualifier is "start" or "end"
        self.digit = digit
        self.qualifier = qualifier

    def __cmp__(self, other):
        # negative if self < other
        # positive self > other
        if self.digit == other.digit and self.qualifier =='s' and other.qualifier!= 's':
            return -1
        elif self.digit < other.digit:
            return -1
        elif self.digit > other.digit:
            return 1
        else:
            return 0

    def __repr__(self):
        return "(" + self.qualifier + str( self.digit ) + ")"

def are_concurrent(I1, I2):
    # start of interval 2 is less that end of interval 1 or viceversa
    return  (I1.start > I2.start and I1.end < I2.end ) \
            or ( I2.start <I1.end and I1.end <I2.end) \
            or (I1.start <I2.end and I2.end < I1.end)

# a is a list of intervals
def tally_concurrent(a):
    concurrent = []

    for i in range(0, len(a)):
        c = [ ]
        c.append(a[i])
        for j in range(i +1, len(a)):
            if are_concurrent(a[i], a[j]):
                c.append(a[j])

        concurrent.append(c)

    return concurrent


def tally_concurrent_better(l):
    max_simultaneous = 0
    counter = 0
    for item in l:
        if item.qualifier =="s":
            counter +=1
        else:
            counter-=1

        if counter > max_simultaneous:
            max_simultaneous = counter

    return max_simultaneous


if __name__=="__main__":

    I1 = Interval(2,3)
    I2 = Interval(4,10)
    I3 = Interval(6,11)
    I4 = Interval(12, 17)
    I5 = Interval(11,13)
    I6 = Interval(2,7)

    a = [I1, I2, I3, I4, I5, I6]
    # o(n), new list creation
    # sort endpoints in ascending order
    l = map(lambda x : [Endpoint(x.start, 's'), Endpoint(x.end, 'e')], a)

    l = [ item for sublist in l for item in sublist]

    # now order , if two endpoints are same start time comes first

    k = l[:]

    l.sort()

    # trying sort

    k.sort(key=lambda x: (x.digit, not x.qualifier == "s"))

    print k
    print l



    print a
    print tally_concurrent(a)

    print tally_concurrent_better(l)
