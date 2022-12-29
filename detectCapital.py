# Detect Capital
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

def detectCapitalUse (word) :
    if word.isupper() :
        return True
    if word.islower() :
        return True
    if word[0].isupper() and word[1:].islower() :
        return True
    else :
        return False
    
print(detectCapitalUse(word="FFFFFg"))
# testcase 1: "USA" should be "true"
# testcase 2: "FlaG" should be "false"
# testcase 3: "leetcode" should be "true"
