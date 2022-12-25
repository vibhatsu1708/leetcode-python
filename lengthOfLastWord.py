# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord (s) :
    length = 0
    str = s.strip()
    for i in range (len(str)) :
        if str[i] != " " :
            length += 1
        else :
            length = 0
    return length
print(lengthOfLastWord(s="luffy is still joyboy"))