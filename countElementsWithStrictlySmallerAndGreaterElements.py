# Count Elements With Strictly Smaller and Greater Elements
# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

def countElements (nums) :
    minNum, maxNum = min(nums), max(nums)
    count = 0
    for i in range (len(nums)) :
        if nums[i] > minNum and nums[i] < maxNum :
            count += 1
    return count
print(countElements(nums = [-71,-71,93,-71,40]))