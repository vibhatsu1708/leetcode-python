# Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sortColors (nums) :
    # Used the selection sort algorithm to achieve the result.
    for i in range (len(nums)) :
        minIndex = i
        for j in range (i+1, len(nums)) :
            if nums[j] < nums[minIndex] :
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums
print(sortColors(nums = [2,0,2,1,1,0]))