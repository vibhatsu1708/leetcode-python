# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    tChars, sChars = {}, {}
    for i in range(len(s)):
        sChars[s[i]] = sChars.get(s[i], 0) + 1
        tChars[t[i]] = tChars.get(t[i], 0) + 1
    for ch in sChars:
        if sChars[ch] != tChars.get(ch, 0):
            return False
    return True
print(isAnagram(s = "anagram", t = "nagaram"))

