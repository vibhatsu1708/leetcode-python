# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr (haystack, needle) :
    first, second = 0, 0
    while (first < len(haystack) and second < len(needle)) :
        if haystack[first] == needle[second] :
            second += 1
        else :
            first -= 1
            second = 0
        first += 1
    if second == len(needle) :
        return first - second
    return -1
print(strStr(haystack = "mississippi", needle = "issip"))
    