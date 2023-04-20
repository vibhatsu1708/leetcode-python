# Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in
# alternating order, starting with word1. If a string is longer than the other, append the additional letters onto
# the end of the merged string. Return the merged string.

def mergeAlternately(word1, word2):
    newstr = ""
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        newstr += word1[i]
        newstr += word2[j]
        i += 1
        j += 1
    if i != len(word1):
        return newstr + word1[i:]
    elif j != len(word2):
        return newstr + word2[j:]
    return newstr

print(mergeAlternately(word1="abcd", word2="pq"))
