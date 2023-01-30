# Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome (s) :
    # Time limit exceeded
    # prefix, suffix = "", ""
    # for i in range (len(s)) :
    #     prefix = s[0:i]
    #     suffix = s[i+1:]
    #     if (prefix+suffix) == (prefix+suffix)[::-1] :
    #         return True
    # return False
    
    # working solution
    left, right = 0, len(s)-1
    while (left < right) :
        if s[left] != s[right] :
            leftSkip, rightSkip = s[left+1 : right+1], s[left:right]
            return (leftSkip == leftSkip[::-1] or rightSkip == rightSkip[::-1])
        left += 1
        right -= 1
    return True
print(validPalindrome(s = "abca"))