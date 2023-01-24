# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber (nums) :
    sum = 0
    for i in range (0, len(nums)+1) :
        sum += i
    for i in range (len(nums)) :
        sum -= nums[i]
    return sum
        
print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))