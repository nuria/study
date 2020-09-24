#!usr/local/bin/python

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            result = []
            result.append([nums[0]])
            result.append([nums[1]])
            result.append(nums)
            return result
        else:
            result = []

            _acumulator = subsets(nums[1:])

            for a in _acumulator:
                result.append([nums[0]] + a)
                result.append(a)

            result.append([nums[0]])

            result.append([])
            return result


# now crazy bit solution
# for a given ordering of the elements of S there exists a one to one correspondence
# between the 2^n bit arrays of length n and the subsets of n so for set [a,b,c] [1,0,1]
# represents [a,c]

import math

def generate_power_set(l):

    cardinal = 1 << len(l)
    # cardinal is the number we are going to get bitmasks for

    result = []

    # cardinal is not binary
    for  bit_array in range(0, cardinal):
        # array with zeros and ones
        s = []
        while bit_array:
            index = math.log(bit_array & ~(bit_array-1) , 2)
            # we can translate this array
            # to a set
            s.append(l[int(index)])
            bit_array = bit_array & (bit_array-1)

        result.append(s)


    return result





if __name__=="__main__":

    print subsets([0,1,2])
    print generate_power_set([0,1,2])
