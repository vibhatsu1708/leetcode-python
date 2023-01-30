# N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

def tribonacci (n) :
    # this solution works
    firstNum, secondNum, thirdNum = 0, 1, 1
    nextNum = 0
    if n == 0 :
        return 0
    if n < 3 :
        return 1
    for i in range (3, n+1) :
        nextNum = firstNum + secondNum + thirdNum
        firstNum = secondNum
        secondNum = thirdNum
        thirdNum = nextNum
    return nextNum
    
    # this solution takes too long.
    # if n == 0 :
    #     return 0
    # if n < 3 :
    #     return 1
    # return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
print(tribonacci(n = 25))