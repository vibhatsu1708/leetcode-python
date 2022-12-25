# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes (nums) :
    count = 0
    i = 0
    while (i < len(nums)) :
        if nums[i] == 0 :
            count += 1
            nums.remove(nums[i])
        else :
            i += 1
    nums.extend([0] * count)
    return nums
        
        
print(moveZeroes(nums=[0,1,0,1,0,3,1,0,2,3,12]))