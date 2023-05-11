# Find the K-Beauty of a Number
# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Note:
# Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

def divisorSubstrings(num, k):
    temp = num
    num = str(num)
    count = 0
    for i in range(len(num) - (k-1)):
        if int(num[i:i+k]) != 0 and temp%int(num[i:i+k]) == 0:
            count += 1
    return count
print(divisorSubstrings(num = 430043, k = 2))