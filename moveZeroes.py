# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes (nums) :
    pointer = 0
    i = 0
    while (i < len(nums)):
        if nums[i] != 0:
            nums[pointer] = nums[i]
            pointer += 1
        i += 1
    for i in range(pointer, len(nums)):
        nums[i] = 0
    return nums
print(moveZeroes(nums = [0,1,0,3,12]))