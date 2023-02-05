# Find the Middle Index in Array
# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

def findMiddleIndex (nums) :
    # for i in range (len(nums)) :
    #     if sum(nums[0:i]) == sum(nums[i+1:]) :
    #         return i
    # return -1
    
    leftSum = 0
    rightSum = sum(nums)
    for i in range (len(nums)) :
        if rightSum - nums[i] == leftSum :
            return i
        leftSum += nums[i]
        rightSum -= nums[i]
    return -1
print(findMiddleIndex(nums = [2,3,-1,8,4]))