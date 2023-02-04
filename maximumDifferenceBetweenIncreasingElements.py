# Maximum Difference Between Increasing Elements
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

def maximumDifference (nums) :
    minNum = nums[0]
    result = -1
    for i in range (1, len(nums)) :
        if nums[i] > minNum :
            result = max(result, nums[i] - minNum)
        minNum = min(minNum, nums[i])
    return result
print(maximumDifference(nums = [7,1,5,4]))