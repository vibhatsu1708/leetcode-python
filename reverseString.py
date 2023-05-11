# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString (s) :
    first, second = 0, len(s)-1
    while (first < second):
        s[first], s[second] = s[second], s[first]
        first += 1
        second -= 1
    return s
print(reverseString(s=["h","e","l","l","o"]))