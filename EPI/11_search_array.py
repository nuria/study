#!usr/local/bin/python
# array returns index i such index and array elemnt are the same
import unittest

def find_equal_entry(a,):
    # o(n) solution loops and looks at all indexes
    # could also do this with binary search if array is sorted
    # key piece of insight is that if A[j] > j and array is sorted no bigger entry in the array
    # will statisfy the condition
    # if A[j] < j no smaller entry will satisfy condition

    if len(a) == 1:
        middle = 0
    else:
        middle = len(a)/2

    if a[middle] > middle:
        # the possible entries might be in first
        return find_equal_entry(a[0:middle])
    elif a[middle] < middle:
        # possible entries are in second
        return find_equal_entry(a[middle:len(a)])
    elif a[middle] == middle:
        return middle




class Testing(unittest.TestCase):
    def test_happy_case(self):
        solution = find_equal_entry([0,10,11,20] )
        print solution
        self.assertEqual(solution , 0 ),


if __name__=="__main__":
    print find_equal_entry([-2,0,2,3,6,7,9])
    unittest.main().result

