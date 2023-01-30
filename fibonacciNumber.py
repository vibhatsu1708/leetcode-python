# Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

def fib (n) :
    firstNum = 0
    secondNum = 1
    temp = 0
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    for i in range (n-1) :
        temp = firstNum + secondNum
        firstNum = secondNum
        secondNum = temp
    return secondNum
print(fib(n = 1))