# Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome (s) :
    s = s.lower()
    str, revstr = "", ""
    for i in range (len(s)) :
        if s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9' :
            str += s[i]
        revstr = str[::-1]
    if revstr == str :
        return True
    else :
        return False
print(isPalindrome(s="0P"))
    