# Consecutive Characters
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.

def maxPower(s):
    if len(s) == 1:
        return 1
    count = 0
    maxCount = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            print(s[i-1], s[i])
            count += 1
        elif s[i-1] != s[i]:
            count = 0
        maxCount = max(maxCount, count)
    return maxCount+1
print(maxPower(s = "jcc"))