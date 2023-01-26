# Add to Array-Form of Integer
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

def addToArrayForm (num, k) :
    numInt = ""
    for i in range (len(num)) :
        numInt += str(num[i])
    numInt = str(int(numInt) + k)
    newNum = []
    for i in range (len(numInt)) :
        newNum.append(int(numInt[i]))
    return newNum
print(addToArrayForm(num = [1,2,0,0], k = 34))