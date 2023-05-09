# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord (s) :
    i = len(s)-1
    count = 0
    while (s[i] == " "):
        i -= 1
    while (i >= 0 and s[i] != " "):
        count += 1
        i -= 1
    return count
print(lengthOfLastWord(s = "   fly me   to   the moon  "))