# Strictly Palindromic Number
# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive),the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.

def isStrictlyPalindromic (n) :
    def checkPalindrome (num, base) :
        newNum = ""
        while (num) :
            newNum = str(num%base) + newNum
            num //= base
        if newNum == newNum[::-1] :
            return True
        return False
    base = 2
    while (base <= (n-2)) :
        if checkPalindrome(n, base) == False :
            return False
        base += 1
        continue
    return True
print(isStrictlyPalindromic(n = 9))