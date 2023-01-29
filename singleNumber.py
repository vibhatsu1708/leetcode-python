# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# This solution uses constant extra space. 
def singleNumber (nums) :
    result = 0
    for num in nums :
        result ^= num
    return result
print(singleNumber(nums=[-1,-1,-2]))