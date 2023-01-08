#!/usr/local/bin


import unittest

class TestSuite(unittest.TestCase):
    def test_happy_case(self):
        t = [5,2,1,6,4,4]
        result = schedule(t)
        self.assertEqual(result, 8)

    def test_happy_2(self):
        t = [1,8,9,10]
        self.assertEqual(schedule(t), 17)

        
# each worker gets assigned two tasks, tasks are independent
# number of worker is ilimited?
def schedule(t):
    result = []
    # T = [5,2,1,6,4,4]
    # sort array and assign longest and shortest to the same worker
    # this might work but might not , hard to prove either way

    t.sort()

    num_workers = len(t)/2

    i = 0
    for w in range(0, num_workers):
        #simple we are not re-scheduling workers just scheduling them once
        tasks = (t[i], t[len(t)-1-i])
        i = i + 1
        result.append(tasks)

    print result 

    result = map(lambda x : x[0] + x[1], result)

    print result 

    return max(result) 

if __name__=="__main__":
    unittest.main().result
