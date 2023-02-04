# Ugly Number
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

def isUgly (n) :
    if n <= 0 :
        return False
    if n == 1 :
        return True
    def keepDividing (dividend, divisor) :
        while dividend%divisor == 0 :
            dividend //= divisor
        return dividend
    for num in [2, 3, 5] :
        n = keepDividing (n, num)
    return (n == 1)
print(isUgly(n = 8))
