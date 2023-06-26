# Number of Beautiful Pairs
# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
# Return the total number of beautiful pairs in nums.
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

import math
def countBeautifulPairs(nums):
    newNums = [str(num) for num in nums]
    count = 0
    def isCoprime(num1, num2):
        return math.gcd(num1, num2) == 1
    for i in range(len(newNums)):
        for j in range(i+1, len(newNums)):
            if isCoprime(int(newNums[i][0]), int(newNums[j][-1])):
                count += 1
    return count
print(countBeautifulPairs(nums = [2,5,1,4]))