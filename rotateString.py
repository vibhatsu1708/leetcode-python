# Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

def rotateString (s, goal) :
    if len(s) != len(goal) :
        return False
    newword = ""
    for i in range (1, len(s)+1) :
        newword = s[i:] + s[0:i]
        if newword == goal :
            return True
    return False
print(rotateString(s = "abcde", goal = "abced"))