# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome (s) :
    left, right = 0, len(s)-1
    while (left < right):
        if s[left] != s[right]:
            skipLeft, skipRight = s[left+1:right+1], s[left, right]
            return (skipLeft == skipLeft[::-1]) or (skipRight == skipRight[::-1])
        left += 1
        right -= 1
    return True
print(validPalindrome(s = "aba"))