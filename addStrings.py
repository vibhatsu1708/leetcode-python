# Add Strings
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

def addStrings (num1, num2) :
    intNum1, intNum2 = 0, 0
    for i in num1 :
        intNum1 = intNum1*10 + (ord(i)-48)
    for i in num2 :
        intNum2 = intNum2*10 + (ord(i)-48)
    return "{}".format(intNum1+intNum2)
print(addStrings(num1="11", num2="123"))