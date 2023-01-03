# Generate a String With Characters That Have Odd Counts
# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

def generateTheString (n) :
    if n == 1 :
        return "a"
    if n%2 == 0:
        return ("a"*(n-1) + "b")
    if n%2 != 0 :
        return ("a"*(n-2) + "b" + "c")
print(generateTheString(n=1))