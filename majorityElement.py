# Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement (nums) :
    count = {}
    for num in nums :
        if num in count : 
            count[num] += 1
        else :
            count[num] = 1
    for i, key in enumerate(count) :
        if count[key] > (len(nums)/2) :
            return key
print(majorityElement(nums=[2,2,1,1,1,2,2]))