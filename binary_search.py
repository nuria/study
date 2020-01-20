#!usr/local/bin

import unittest

def binary_search(item, a):
    # base case
    l = len(a)
    if  l==1 and a[0] == item:
        return item
    elif l == 0:
        return -1

    # split a in half
    first = a[0:l/2]
    second = a[l/2: l]
    # is item in first
    if first[0] <= item and first[len(first)-1] >= item:
        return binary_search(item, first)
    elif second[0] <= item and second[len(second)-1] >= item:
        return binary_search(item, second)
    else:
        return -1

def iterative_binary_search(item, a):
    # set indexes for left and right arrays
    left, right = 0, len(a) -1

    while left <= right:
        middle = (left + right)/2
        if A[middle] < item:
            left = midlle +1
        elif A[middle] > item
            right = middle  -1
        else:
            return M

    return -1



class testing(unittest.TestCase):
    def test_happy_case(self):
        a = [i for i in range(0, 255)]
        self.assertEqual(binary_search(100,a), 100)

    def test_empty(self):
        a = []
        self.assertEqual(binary_search(100, a), -1)

    def test_not_present(self):
        a = [i for i in range(0, 255)]
        self.assertEqual(binary_search(1001,a), -1)


if __name__=="__main__":

    unittest.main().result
