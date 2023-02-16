# Count Integers With Even Digit Sum
# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.

def countEven (num) :
    def isEvenSum (digit) :
        sum = 0
        while (digit > 0) :
            sum += digit%10
            digit //= 10
        if sum%2 == 0 :
            return True
        return False
    count = 0
    for digit in range (1, num+1) : 
        if isEvenSum(digit) :
            count += 1
    return count
print(countEven(num = 30))