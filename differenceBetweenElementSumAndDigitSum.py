# Difference Between Element Sum and Digit Sum of an Array
# You are given a positive integer array nums.
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.

def differenceOfSum (nums) :
    elementSum, digitSum = 0, 0
    for num in nums : 
        elementSum += num
        temp = num
        while temp > 0 :
            remainder = temp % 10
            digitSum += remainder
            temp //= 10
    return abs(elementSum - digitSum)
print(differenceOfSum(nums=[1,2,3,4]))