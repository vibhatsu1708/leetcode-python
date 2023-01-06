# Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternately (word1, word2) :
    resultStr = ""
    i = 0
    while (i<len(word1) or i<len(word2)) :
        if i < len(word1) :
            resultStr += word1[i]
        if i < len(word2) :
            resultStr += word2[i]
        i += 1
    return resultStr
        
print(mergeAlternately(word1="abc", word2="pqr"))