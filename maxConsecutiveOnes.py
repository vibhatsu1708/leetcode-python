# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes (nums) :
    count = 0
    maxCount = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        elif nums[i] == 0:
            count = 0
        maxCount = max(maxCount, count)
    return maxCount
print(findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))