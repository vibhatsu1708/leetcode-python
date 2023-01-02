# Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

def firstPalindrome (words) :
    firstPalindrome = ""
    for word in words :
        revword = word[::-1]
        if revword == word :
            firstPalindrome = word 
            break
    return firstPalindrome
print(firstPalindrome(words=["def","ghi"]))
        