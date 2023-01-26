# Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

def maximumProduct (nums) :
    nums.sort()
    maxProduct = max([nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3]])
    return maxProduct, nums
print(maximumProduct(nums=[-1,-2,1,2,3]))