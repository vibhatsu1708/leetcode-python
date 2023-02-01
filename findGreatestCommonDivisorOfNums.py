# Find Greatest Common Divisor of Array
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

def findGCD (nums) :
    minNum, maxNum = nums[0], nums[0]
    gcd = 1
    for num in nums :
        if minNum > num :
            minNum = num
        if maxNum < num :
            maxNum = num
    for i in range (1, minNum+1) :
        if minNum%i == 0 and maxNum%i == 0 :
            gcd = i
    return gcd
print(findGCD(nums = [2,5,6,9,10]))