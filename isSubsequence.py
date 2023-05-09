# Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    left, right = 0, 0
    while (left < len(s) and right < len(t)):
        if s[left] == t[right]:
            left += 1
            right += 1
        else:
            right += 1
    return left == len(s)
print(isSubsequence(s = "abc", t = "ahbgdc"))