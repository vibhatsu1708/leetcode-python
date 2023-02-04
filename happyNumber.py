# Happy Number
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy (n) :
    def getSquare (n) :
        totalSum = 0
        while (n > 0) :
            remainder = n%10
            totalSum += remainder**2
            n //= 10
        return totalSum
    squares = set()
    while (n != 1 and n not in squares) :
        squares.add(n)
        n = getSquare(n)
    return (n == 1)
print(isHappy(n = 2))