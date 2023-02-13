# Number of Steps to Reduce a Number to Zero
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps (num) :
    count = 0
    while (num) :
        if num%2 == 0 :
            count += 1
            num //= 2
        else :
            count += 1
            num -= 1
    return count
print(numberOfSteps(num = 8))