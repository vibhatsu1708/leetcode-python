# Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

def multiply (num1, num2) :
    intNum1, intNum2 = 0, 0
    for digit in num1 :
        intNum1 = intNum1*10 + (ord(digit)-48)
    for digit in num2 :
        intNum2 = intNum2*10 + (ord(digit)-48)
    return "{}".format(intNum1*intNum2)
print(multiply(num1 = "11", num2 = "123"))