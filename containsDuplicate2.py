# Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate (nums, k) :
    seen = {}
    for i in range (len(nums)) :
        if nums[i] not in seen :
            seen[nums[i]] = i
        else :
            if i - seen[nums[i]] <= k :
                return True
    return False
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))