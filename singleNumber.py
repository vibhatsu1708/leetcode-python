# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber (nums) :
    count = {}
    for num in nums :
        if num in count :
            count[num] += 1
        else :
            count[num] = 1
    for i, key in enumerate(count) :
        if count[key] == 1 :
            return key
print(singleNumber(nums=[1]))