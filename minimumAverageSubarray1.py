# Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

def findMaxAverage(nums, k):
    windowAverage = sum(nums[:k])/k
    maxAverage = windowAverage
    for i in range(len(nums) - k):
        windowAverage = (windowAverage*k - nums[i] + nums[i+k])/k
        maxAverage = max(windowAverage, maxAverage)
    return maxAverage
print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))