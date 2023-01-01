# Reverse Prefix of Word
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

def reversePrefix (word, ch) :
    prefix, revprefix = "", ""
    newword = ""
    address = 0
    for i in range (len(word)) :
        if word[i] == ch :
            address = i+1
            prefix = word[0:i+1]
            break
    revprefix = prefix[::-1] + word[address:]
    return revprefix
print(reversePrefix(word="xyxzxe", ch="z"))