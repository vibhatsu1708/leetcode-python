# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum (nums) :
    rsum = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        rsum.append(sum)
    return rsum
        
print(runningSum(nums=[3,1,2,10,1]))