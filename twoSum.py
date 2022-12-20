# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSum (nums, target) :
    indices = {}
    for i, num in enumerate(nums) :
        difference = target-num 
        if (difference) in indices : 
            return [indices[difference], i]
        indices[num] = i
    return []

print(twoSum(nums=[2,7,11,15], target=9))
