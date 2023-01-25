# A Number After a Double Reversal
# Reversing an integer means to reverse all its digits.
# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

def isSameAfterReversals (num) :
    temp = num
    reverse, doubleReverse = 0, 0
    while (temp != 0) :
        remainder = temp % 10
        reverse = reverse*10 + remainder
        temp //= 10
    temp = reverse
    while (temp != 0) :
        remainder = temp % 10
        doubleReverse = doubleReverse*10 + remainder
        temp //= 10
    if doubleReverse == num :
        return True
    else :
        return False
print(isSameAfterReversals(num = 0))