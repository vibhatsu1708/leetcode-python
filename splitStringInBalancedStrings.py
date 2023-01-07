# Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

def balancedStringSplit (s) :
    substrings = 0
    count = {
        "R": 0,
        "L": 0
    }
    for ch in s :
        count[ch] += 1
        if count["R"] == count["L"] :
            substrings += 1
    return substrings
    
print(balancedStringSplit(s="LLLLRRRR"))