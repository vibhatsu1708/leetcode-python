# Find the Value of the Partition
# You are given a positive integer array nums.

# Partition nums into two arrays, nums1 and nums2, such that:

# Each element of the array nums belongs to either the array nums1 or the array nums2.
# Both arrays are non-empty.
# The value of the partition is minimized.
# The value of the partition is |max(nums1) - min(nums2)|.

# Here, max(nums1) denotes the maximum element of the array nums1, and min(nums2) denotes the minimum element of the array nums2.

# Return the integer denoting the value of such partition.

def findValueOfPartition(nums):
    nums = sorted(nums)
    minDiff = float("inf")
    diff = nums[0]
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        minDiff = min(diff, minDiff)
    return minDiff
print(findValueOfPartition(nums = [1,3,2,4]))