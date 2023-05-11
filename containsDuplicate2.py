# Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate (nums, k) :
    count = {}
    for index, num in enumerate(nums):
        if num in count and abs(index - count[num]) <= k:
            return True
        count[num] = index
    return False
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))