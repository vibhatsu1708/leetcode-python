# Minimum Difference Between Highest and Lowest of K Scores
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

def minimumDifference(nums, k):
    nums = sorted(nums)
    left, right = 0, k-1
    minDiff = float("inf")
    while (right < len(nums)):
        minDiff = min(minDiff, abs(nums[left] - nums[right]))
        left += 1
        right += 1
    return minDiff
print(minimumDifference(nums = [9,4,1,7], k = 2))