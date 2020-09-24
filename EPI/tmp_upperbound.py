#!/usr/bin/python
# given an API for a very large array that returns either the element at index i
# or OOB exception if i bigger than length
# find upper bound of array

class OOBException(Exception):
    pass

class API():

    def __init__(self, value):
        self.value = value

    def get(self, i):
        #simple
        if i > self.value:
            raise OOBException
        else:
            return i



# isnt't this kind of like binary search in the whole integer range?
# interval is a tuple (lower, upper)
def find_OOB(A, interval):

    # assuming upper is always OOB

    print interval

    (lower, upper) = interval

    try:
        value = A.get(lower)
        if upper-lower == 1:
            # base case found value
            return lower
        else:
            # need to tight the interval
            # moving lower forward, upper (OOB stays)
            return find_OOB(A, (lower + (upper-lower)/2, upper))


    except OOBException:
         # lower bound is too high, moving lower back
         print "exception"
         if upper-lower  == 1:
            return find_OOB(A,(lower -1,lower))

         else:
            return find_OOB(A ,( lower - (upper-lower)/2 , lower))



if __name__ =="__main__":

    api = API(100532)

    # go with powers of 10 and find teh first one that returns an OOB
    upper = 10
    while (True):
        try:
            api.get(upper)
            upper = upper * 10
        except OOBException:
            break

    print find_OOB(api, (0,upper ))

