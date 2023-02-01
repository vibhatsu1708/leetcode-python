# Three Divisors
# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
# An integer m is a divisor of n if there exists an integer k such that n = k * m.

def isThree (n) :
    # divisors = []
    # for i in range (1, n+1) :
    #     if n%i == 0 :
    #         divisors.append(i)
    # if len(divisors) == 3 :
    #     return True
    # return False
    
    count = 0
    for i in range (1, n+1) :
        if n%i == 0 :
            count += 1
    return count == 3
print(isThree(n = 4))