# Convert Integer to the Sum of Two No-Zero Integers
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
# Given an integer n, return a list of two integers [a, b] where:
# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

def getNoZeroIntegers (n) :
    # function to check num using strings
    # returns true if 0 is not in num.
    # returns false in the other case.
    # def isNumZero (num) :
    #     if "0" in str(num) :
    #         return False
    #     return True
    
    # function to check num without using strings
    def isNumZero (num) :
        while (num) :
            if num%10 == 0 :
                return False
            num //= 10
        return True
    
    left, right = 1, n-1
    while (left <= right) :
        if isNumZero (left) and isNumZero (right) :
            return [left, right]
        left += 1
        right -= 1
print(getNoZeroIntegers(n = 101))