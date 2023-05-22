# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    leftProd, rightProd = [0] * len(nums), [0] * len(nums)
    leftProd[0], rightProd[-1] = 1, 1
    for i in range(1, len(nums)):
        leftProd[i] = leftProd[i-1] * nums[i-1]
    for i in range(len(nums)-2, -1, -1):
        rightProd[i] = rightProd[i+1] * nums[i+1]
    result = [0] * len(nums)
    for i in range(len(nums)):
        result[i] = (leftProd[i] * rightProd[i])
    return result
print(productExceptSelf(nums = [1,2,3,4]))