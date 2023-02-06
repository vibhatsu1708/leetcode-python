# Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

def isPerfectSquare (num) :
    low, high = 1, num
    while (high - low) > 1 :
        mid = (high + low) // 2
        if num == 1 :
            return True
        if (mid * mid) == num :
            return True
        elif (mid * mid) > num :
            high = mid - 1
        elif (mid * mid) < num :
            low = mid + 1
    if low * low == num or high * high == num :
        return True
    return False
print(isPerfectSquare(num = 1))