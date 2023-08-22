#!/usr/local/lib

def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        
        while len(stack) > 0  and nums[i] > nums[stack[-1]]:
            
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result



# Example usage
nums = [4, 5, 2, 25, 7, 18]
result = next_greater_element(nums)
print("Input Array: ", nums)
print("Next Greater Elements: ", result)
