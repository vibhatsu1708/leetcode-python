# Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits

def subtractProductAndSum (n) :
    temp = n
    sumOfDigits, productOfDigits = 0, 1
    while (temp > 0) :
        remainder = temp%10
        sumOfDigits += remainder
        productOfDigits *= remainder
        temp //= 10
    return productOfDigits - sumOfDigits
print(subtractProductAndSum(n=4421))