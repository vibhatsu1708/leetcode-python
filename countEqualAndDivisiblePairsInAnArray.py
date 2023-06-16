# Count Equal and Divisible Pairs in an Array
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

def countPairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] == nums[j] and (i*j)%k == 0:
                    count += 1
    return count
print(countPairs(nums = [1,2,3,4], k = 1))