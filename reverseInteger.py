# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse (x) :
    temp = abs(x)
    reverse = 0
    while (temp > 0) :
        remainder = temp % 10
        reverse = reverse*10 + remainder
        temp //= 10
    if reverse < -(2**31)-1 or reverse > (2**31) :
        return 0
    else :
        if x < 0 :
            return -reverse
        else :
            return reverse
    
print(reverse(x=1534236469))