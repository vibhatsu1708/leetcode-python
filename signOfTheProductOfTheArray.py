# Sign of the Product of an Array
# There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

def arraySign (nums) :
    prod = 1
    for digit in nums : prod *= digit
    if prod > 0 : return 1
    if prod < 0 : return -1
    if prod == 0 : return 0
print(arraySign(nums=[-1,1,-1,1,-1]))