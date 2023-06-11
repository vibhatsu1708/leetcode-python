# Check if The Number is Fascinating
# You are given an integer n that consists of exactly 3 digits.

# We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:

# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.

# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

def isFascinating(n):
    ideal = [i for i in range(1, 10)]
    num = str(n) + str(2*n) + str(3*n)
    num = [int(i) for i in num]
    num = sorted(num)
    return ideal == num
print(isFascinating(n = 100))