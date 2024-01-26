#!/usr/local/lib
import unittest



def mergeIntervals(schedule):
    S = sorted(schedule)
    
    # it can be x0, y0 x1, y1
    # [x0,y0] 
    # ....[x1, y1]
    # [x0,       y0]
    # ....[x1,y1]

    result = []
    
   
    # if they overlap x1 <= y0 => bounds (x0, max(y0, y1))

    p1 = 0
   
    (x0, y0) = schedule[0]

    while p1 <len(schedule)-1:
        # we add intervals that do not overlap to resultset
        p2 = p1 + 1
        (x1, y1) = schedule[p2]
        if x1 <= y0:
            # merge
            (x0,y0) = (x0, max(y0,y1))
        else:
            #no merge
            result.append((x0,y0))
            (x0, y0) = (x1, y1)
        
        p1 = p2
        

        if p2 == len(schedule)-1:
            result.append((x0,y0))
            break


    return result

        
    



class TestCase(unittest.TestCase):
    def test_happy_case_no_overlap(self):
          self.assertEqual(mergeIntervals([(9, 10), (11, 17), (23, 35)]),[(9, 10), (11, 17), (23, 35)])


    def test_happy_case_overlap(self):
          self.assertEqual(mergeIntervals([(9, 11), (10, 12), (13, 15)]),[(9, 12), (13, 15)])

    def test_happy_case_overlap_completely(self):
          self.assertEqual(mergeIntervals([(9, 20), (10, 12), (13, 15)]),[(9, 20)])

if __name__=="__main__":
    unittest.main().result




