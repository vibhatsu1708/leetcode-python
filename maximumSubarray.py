# Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray (nums) :
    sum, maximumSum = 0, -10**4
    for num in nums :
        sum += num
        maximumSum = max(maximumSum, sum)
    return maximumSum
print(maxSubArray(nums = [-1]))