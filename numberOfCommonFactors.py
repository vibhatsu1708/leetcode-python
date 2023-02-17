# Number of Common Factors
# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

def commonFactors (a, b) :
    count = 0
    minNum = min(a, b)
    for i in range (1, minNum+1) :
        if a%i == 0 and b%i == 0 :
            count += 1
    return count
print(commonFactors(a = 25, b = 30))