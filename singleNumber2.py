# Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber (nums) :
    count = {}
    for i in range (len(nums)) :
        if nums[i] not in count :
            count[nums[i]] = 1
        else :
            count[nums[i]] += 1
    for i, value in enumerate (count) :
        if count[value] == 1 :
            return value
print(singleNumber(nums=[0,1,0,1,0,1,99]))