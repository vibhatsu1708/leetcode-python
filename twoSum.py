# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    dictMap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in dictMap:
            return [dictMap[diff], index]
        dictMap[num] = index
print(twoSum(nums = [3,2,4], target = 6))