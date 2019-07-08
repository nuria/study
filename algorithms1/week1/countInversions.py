#!/usr/local/lib/python

import sys
import ast

import unittest

# no checks for types.. etc
# returns list sorted
def mergeSorted(a, b, inver):
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
            inver = inver + len(a)-i
            j = j+1;
        else:
            result.append(a[i])
            result.append(b[j])
            k = k+ 1
            i = i+1
            j = j +1
        k = k +1

    return (result, inver)


def splitList(l):
    size = len(l);
    if size == 1:
        return l;
    middle = size/2
    first = l[0:middle]
    second = l[middle:size]
    return first,second


def mergeSort(l,inversions=0):
    if len(l) == 1:
        return l,0
    first , second = splitList(l)
    f,i1 = mergeSort(first)
    s,i2 = mergeSort(second)
    return mergeSorted(f, s, i1+i2)


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


    def test_mergeSorted(self):
        a = [1,3,5]
        b = [2,4,6]
        r, i = mergeSorted(a,b,0)
        print ("input {0} {1}, output {2} inversions {3}").format(a,b,r,i)


    def test_merge(self):
        l = [1,2,3,4,5]
        s,i = mergeSort(l)

        print ("input {0}, output {1} inversions {2}".format(l,s,i))

        l = [6,7,8,1,2]
        s,i = mergeSort(l)
        print ("input {0}, output {1}, inversions {2}".format(l,s,i))

        l = [1,3,5,2,4,6]
        s,i = mergeSort(l)
        print ("input {0}, output {1} inversions {2}".format(l,s,i))

        l = [7,6,5,4,3,2,1]
        s, i = mergeSort(l)
        print ("input {0}, output {1} inversions {2}".format(l,s,i))

if __name__ =="__main__":
    unittest.main()
