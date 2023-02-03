# Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def search (nums, target) :
    if len(nums) == 0 : 
        return -1
    start, end = 0, len(nums)-1
    while (start <= end) :
        mid = (start + end)//2
        if nums[mid] == target :
            return mid
        elif nums[mid] > target :
            end = mid - 1
        elif nums[mid] < target :
            start = mid + 1
    return -1
print(search(nums = [2,5], target = 5))