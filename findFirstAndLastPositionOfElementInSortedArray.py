# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

def searchRange (nums, target) :
    targetAddresses = []
    if target not in nums :
        return [-1, -1]
    for i in range (len(nums)) :
        if target == nums[i] :
            targetAddresses.append(i)
    return [targetAddresses[0], targetAddresses[-1]]
print(searchRange(nums=[5,7,7,8,8,10], target=8))