# Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers (nums) :
    count = {}
    result = []
    for i in range(1, len(nums)+1):
        count[i] = count.get(nums[i-1], 0) 
    for num in nums:
        if num in count:
            count[num] += 1
    for key, value in count.items():
        if value == 0:
            result.append(key);
    return result
print(findDisappearedNumbers(nums = [1,1]))