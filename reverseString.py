# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString (s) :
    for i in range (len(s)) :
        ch = s.pop()
        s.insert(i, ch)
    return s

# functioning of the program, 
# loops through the array, and individually pops each and every element, and stores that element in a variable.
# once stored, that variable's value is stored at the ith position of the same array from the beginning.
    
print(reverseString(s=["h","e","l","l","o"]))

"""
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

"""
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""