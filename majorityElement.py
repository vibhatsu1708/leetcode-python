# Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement (nums) :
    count = {}
    n = len(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key, value in count.items():
        if value > (n/2):
            return key
print(majorityElement(nums = [3,2,3]))