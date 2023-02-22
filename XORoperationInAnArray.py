# XOR Operation in an Array
# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

def xorOperation (n, start) :
    sum = start
    i = 1
    while (i < n) :
        sum ^= (start + 2 * i)
        i += 1
    return sum
print(xorOperation(n = 5, start = 0))