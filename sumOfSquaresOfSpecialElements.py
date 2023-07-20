# Sum of Squares of Special ElementsYou are given a 1-indexed integer array nums of length n.

# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

# Return the sum of the squares of all special elements of nums.

def sumOfSquares(nums):
    result = 0
    for i in range(1, len(nums)+1):
        if len(nums)%i == 0:
            result += nums[i-1]**2
    return result
print(sumOfSquares(nums = [2,7,1,19,18,3]))