#!usr/local/bin/python
# coding : utf-8
"""
Given a sorted array arr of distinct integers,
write a function indexEqualsValueSearch that
returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index.
Analyze the time and space complexities of your solution and explain its correctness.

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1


"""
def binary_search(arr):

    # without recursion
    L, U = 0, len(arr)

    while L <= U:



        middle = (U-L)/2

        item = arr[middle]

        print "{0}, {1} {2} {3}".format( L, U, middle, item)

        if item < arr[middle]:
            # move forward
            L = middle + 1
        elif middle == item:
            return middle
        else:
            # move back
            U = middle -1

    return -1



if __name__=="__main__":
    print binary_search([0,3])
    print "answer should be 3"
    print binary_search([-8,0,1,3,5])
    print binary_search([-8,0,2,5])
