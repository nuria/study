#!/usr/local/bin
import sys

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
so [3,0,1] returns 2
and [9,6,4,2,3,5,7,0,1] returns 8
"""

def main():
    nums = eval(sys.argv[1])

    
    def _find(nums, _max, _min):
        print "nums:{0} , max:{1}, min:{2}".format(nums, _max, _min)

        l = len(nums)
        # min set is 2 numbers
        if l == 2 and _max-_min + 1 != l:
            # we are missing one number
            if _max not in nums:
                return _max
            elif _max-1 not in nums:
                return _max-1
            else:
                return _max-2
        # we have more that two elements on list 
        p = nums[0]
        
        right = []
        
        left = []
    
        min_right = float('inf')

        for n in nums:
            # split the list in two 
            # carry values of min/max
            if n == p :
                continue
            if n < p:
                left.append(n)
            else:
                if n < min_right:
                    min_right = n
                right.append(n)

        # just changes order so 1st iteration is [3,0,1] => left [0,1,3]
        # and second will be [0,1,3] => left [0] , right [1,3]
        left.append(p)

        print " left: {0}, right:{1}". format(left, right)
        
        
        # only 1 branch needs traversing
        if len(left) > 1 and p-_min +1 != len(left):
            return _find(left,p,_min)
        elif len(right) > 1: # this should not happen
            return _find(right,_max, min_right) 


    print _find(nums, len(nums),0)
        
if __name__=="__main__":
    main()
