# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    countSet = set()
    for num in nums:
        if num in countSet:
            return True
        else:
            countSet.add(num)
    return False
print(containsDuplicate(nums = [1,2,3,1]))