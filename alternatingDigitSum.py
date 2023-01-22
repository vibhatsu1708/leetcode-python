# Alternating Digit Sum
# You are given a positive integer n. Each digit of n has a sign according to the following rules:
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

def alternateDigitSum (n) :
    temp = str(n)
    sum = 0
    for i in range (len(temp)) :
        if i%2 == 0 :
           sum += int(temp[i]) 
        if i%2 != 0 :
            sum -= int(temp[i])
    return sum
        
print(alternateDigitSum(n = 886996))