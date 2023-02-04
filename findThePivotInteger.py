# Find the Pivot Integer
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

def pivotInteger (n) :
    if n <= 1 :
        return n
    numbers = [num for num in range (1, n+1)]
    for i in range (len(numbers)) :
        if sum(numbers[0:i]) == sum(numbers[i+1:]) :
            return numbers[i]
    return -1 
print(pivotInteger(n = 4))