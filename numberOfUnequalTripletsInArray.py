# Number of Unequal Triplets in Array
# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:
# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.

def unequalTriplets (nums) :
    count = 0
    for i in range (len(nums)) :
        for j in range (i+1, len(nums)) :
            for k in range (j+1, len(nums)) :
                if (nums[i] > 0 and nums[j] > 0 and nums[k] > 0) and ((nums[i] != nums[j]) and (nums[j] != nums[k]) and (nums[i] != nums[k])) :
                    count += 1
    return count
print(unequalTriplets(nums = [1,1,1,1,1]))