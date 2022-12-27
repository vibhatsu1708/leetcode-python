# Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne (digits) :
    digitsStr = ""
    newdigits = []
    for digit in digits :
        digitsStr += str(digit)
    digitsStr = int(digitsStr) + 1
    for digit in str(digitsStr) :
        newdigits.append(int(digit))
    return newdigits
print(plusOne(digits=[4,3,2,1]))
    