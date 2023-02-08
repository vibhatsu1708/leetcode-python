# Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

def backspaceCompare (s, t) :
    def buildStr (temp) :
        result = []
        for ch in temp :
            if ch != "#" :
                result.append(ch)
            elif result :
                result.pop()
        return result
    return buildStr(s) == buildStr(t)
print(backspaceCompare(s = "a#c", t = "b"))