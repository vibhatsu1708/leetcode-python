# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate (nums, k) :
    # swap the elements, but after swapping they'll be in reverse order.
    left, right = 0, len(nums)-1
    while (left < right) :
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    # now the next steps are to reverse the reversed elements.
    
    # # reverse the elements from 0 till k-1.
    # k = k % len(nums) # if k goes beyong the length of the input array.
    # left, right = 0, k-1
    # while (left < right) :
    #     nums[left], nums[right] = nums[right], nums[left]
    #     left += 1
    #     right -= 1
    
    # # and now reverse the elements from kth position to len(nums)-1.
    # left, right = k, len(nums)-1
    # while (left < right) :
    #     nums[left], nums[right] = nums[right], nums[left]
    #     left += 1
    #     right -= 1
    
    def reverseNums (left, right) :
        while (left < right) :
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    reverseNums(0, k-1)
    reverseNums(k, len(nums)-1)
    return nums    
print(rotate(nums = [1,2,3,4,5,6,7], k = 3))