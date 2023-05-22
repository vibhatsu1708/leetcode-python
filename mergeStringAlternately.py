# Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in
# alternating order, starting with word1. If a string is longer than the other, append the additional letters onto
# the end of the merged string. Return the merged string.

def mergeAlternately(word1, word2):
    result = ""
    left, right = 0, 0
    while (left < len(word1) and right < len(word2)):
        result += word1[left] + word2[right]
        left += 1
        right += 1
    if left != len(word1):
        return result + word1[left:]
    if right != len(word2):
        return result + word2[right:]
    else:
        return result
print(mergeAlternately(word1 = "ab", word2 = "pqrs"))
