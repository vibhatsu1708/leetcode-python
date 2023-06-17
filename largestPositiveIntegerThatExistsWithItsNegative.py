# Largest Positive Integer That Exists With Its Negative
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

def findMaxK(nums):
    count = {}
    for num in nums:
        if num > 0 and -num in nums:
            count[num] = True
    maxNumber = -1
    for num, _ in count.items():
        maxNumber = max(num, maxNumber)
    return maxNumber
print(findMaxK(nums = [-1,10,6,7,-7,1]))