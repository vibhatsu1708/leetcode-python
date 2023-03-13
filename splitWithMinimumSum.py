# Split With Minimum Sum
# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
# Notes:
# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

def splitNum (num) :
    num = sorted(str(num))
    num1, num2 = "", ""
    for i in range (0, len(num), 2) :
        num1 += num[i]
    for j in range (1, len(num), 2) :
        num2 += num[j]
    return int(num1) + int(num2)
print(splitNum(num = 687))
    