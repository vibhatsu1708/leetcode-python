# Count the Digits That Divide a Number
# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

def countDigits (num) :
    count = 0
    temp = str(num)
    for ch in temp :
        if num%int(ch) == 0 :
            count += 1
            continue
    return count
print(countDigits(num = 121))