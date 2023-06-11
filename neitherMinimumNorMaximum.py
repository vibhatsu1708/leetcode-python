# Neither Minimum nor Maximum
# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
# Return the selected integer.

def findNonMinOrMax(nums):
    if len(nums) <= 2:
        return -1
    else:
        nums = sorted(nums)
        return nums[1]
print(findNonMinOrMax(nums = [3,2,1,4]))