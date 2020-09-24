#!usr/local/bin/python
# coding: utf-8
"""
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.
"""



def solve(A):

    if len(A) == 2:
        return [A[1], A[0]]


    result = []

    l = len(A)

    L = []

    R = [1] * l

    L.append(1)


    for i in range(1, l):
        L.append( L[i-1] * A[i -1])

    for i in range(l -2, -1, -1):
        R[i] = R[i + 1] * A[i +1]


    for i in range(0, l):
        result.append(L[i] * R[i])

    return result


if __name__=="__main__":
    A =  [8, 10, 2]
    # solution
    # output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]
    A= [2, 7, 3, 4]
    #[84, 24, 56, 42]
    print solve(A)


