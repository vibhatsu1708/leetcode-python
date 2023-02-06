# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

def palindromeNumber (x) :
    temp = abs(x)
    palindromeNum = 0
    while (temp > 0) :
        remainder = temp%10
        palindromeNum = palindromeNum*10 + remainder
        temp //= 10
    if palindromeNum == x :
        return True
    else :
        return False
print(palindromeNumber(10))