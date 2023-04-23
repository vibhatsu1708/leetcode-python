# Intersection of Multiple Arrays
# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

def intersection(nums):
    elements = nums[0]
    newElements = elements[:]
    for row in nums:
        newElements = set(row) & set(newElements)
    return sorted(list(newElements))
print(intersection(nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))