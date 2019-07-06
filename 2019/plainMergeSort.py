#!/usr/local/lib/python

# implementation of merge sort, how long does it take?
# python mergeSort.py '[1,2,3]'
import sys
import ast

import unittest

# no checks for types.. etc
# returns list sorted
def mergeSorted(a, b):
    result = []
    i = 0
    j = 0
    k = 0
    while k < len(a)+ len(b):

        if i >= len(a):
            result.extend(b[j:len(b)])
            break;
        if j >= len(b):
            result.extend(a[i:len(a)])
            break;

        if a[i] < b[j]:
            result.append(a[i])
            i = i+1
        elif a[i] > b[j]:
            result.append(b[j])
            j = j+1;
        else:
            result.append(a[i])
            result.append(b[j])
            k = k+ 1
            i = i+1
            j = j +1
        k = k +1

    return result


def splitList(l):
    size = len(l);
    if size == 1:
        return l;
    middle = size/2
    first = l[0:middle]
    second = l[middle:size]
    return first,second


def mergeSort(l):
    if len(l) == 1:
        return l
    first , second = splitList(l)
    return mergeSorted(mergeSort(first), mergeSort(second))



# reading input list from command line
#l = ast.literal_eval(sys.argv[1])
#print ("input {0}".format(l))


class TestMergeSort(unittest.TestCase):

    def test_happycase(self):
        self.assertTrue(True)
        print "happy"

    def test_split(self):
        l = [1,2,3,4,5]
        f, s = splitList(l)
        self.assertTrue(len(f),2)
        self.assertTrue(len(s),3)
        l = [1,2]
        f, s = splitList(l)
        self.assertTrue(len(f),1)
        self.assertTrue(len(s),1)
        l = [1]
        f = splitList(l)
        self.assertTrue(len(f),1)

    def test_merge(self):
        l = [1,2,3,4,5]
        s = mergeSort(l)
        print ("input {0}, output {1}".format(l,s))
        l = [6,7,8,1,2]
        s = mergeSort(l)
        print ("input {0}, output {1}".format(l,s))

if __name__ =="__main__":
    unittest.main()
