# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate (nums) :
    seen = {}
    for num in nums :
        if num in seen :
            return num
        else :
            seen[num] = 1
print(findDuplicate(nums = [2,2,2,2,2]))