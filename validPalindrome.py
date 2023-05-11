# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    s = s.lower()
    newS = ""
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122 or ord(s[i]) >= 48 and ord(s[i]) <= 57:
            newS += s[i]
    revStr = newS[::-1]
    return newS == revStr
print(isPalindrome(s = " 0P"))
    