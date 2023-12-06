#!/usr/local/bin

import sys
import unittest
# part 2 is a bit harder and had to look at https://www.reddit.com/r/adventofcode/comments/18b4b0r/2023_day_5_solutions/
# for ideas

# returns true if the seed range contains the candidate
def valid_seed(seeds, candidate):
    i = 0
    while(i < len(seeds)-1):
        if seeds[i] <= candidate  and candidate < seeds[i]+ seeds[i+1]:
            return True
        i = i +  2
    
    return False

def get_destination(data,source):
    #print(source)
    candidate = float('inf')
    destination = None
    for k in data:
        (d, s, r) = k
        #print ("({0}, {1},{2})".format(d,s,r))
        
        if s<= source and source < s + r:
             if (source-s) < candidate:
                destination = d + (source-s)

    if destination is None:
        return source
    else:
        return destination


def main():

    data = []
    f = open(sys.argv[1])
    
    # execute test like python day5 [79, 14, 55,13] 
   
    seeds = [79,14,55,13]

    #print (seeds)
    
    seeds = [2149186375,163827995,1217693442,67424215,365381741,74637275,1627905362,77016740,22956580,60539394,586585112,391263016,2740196667,355728559,2326609724,132259842,2479354214,184627854,3683286274,337630529]
    

    data = None
    path = []

    EMPTY = ""

    for l in f:
        l = l.strip()
        
        if l.strip() == EMPTY:
            if data is not None:
                    path.append(data)
            data = []
            continue


        # numeric line
        #(d, s, r) = l.split()
        
        # we revert that 
        (s, d, r) = l.split()
        destination = int(d)
        source = int(s)
        r = int(r)
        data.append((destination,source,r))
    


    
    # now start walking back from the minimumn set on destination
    #print (path)
    
    path = list(reversed(path))

    found = False
    
    i = 0
    while not found:
        
        candidate = i
        # not quite binary search 
        for  data in path:
            # walk backwards 
            candidate = get_destination(data, candidate)
            #print("candidate: {0}".format(candidate))
        if valid_seed(seeds, candidate):
            found = True
            break

        i = i + 1

    
    print("the seed :{0} , the candidate:{1}".format(i, candidate))


class TestCase(unittest.TestCase):
    def test_happy_ranges(self):
        """
        # destination source range
        50 98 2
        52 50 48
        """
        # destination 98
        # source 50
        # range 2
        # are we modeling this like a graph
        # easiest to start is to have a hash with key values
        destinations = [79, 14, 55, 13]
        
        data = [(50,98,2),(52,50,48)]
        
        self.assertTrue(get_destination(data,99)==51)
        self.assertTrue(get_destination(data,98)==50)

        self.assertTrue(get_destination(data,53)==55)
        self.assertTrue(get_destination(data,79)==81)

        self.assertTrue(get_destination(data, 14)==14)


if __name__=="__main__":
    main()
    #unittest.main().result
