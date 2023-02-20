# Check Whether Two Strings are Almost Equivalent
# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
# The frequency of a letter x is the number of times it occurs in the string.

def checkAlmostEquivalent (word1, word2) :
    count = {}
    for ch in word1 :
        if ch not in count :
            count[ch] = 1
        else :
            count[ch] += 1
    for ch in word2 :
        if ch not in count :
            count[ch] = -1
        else :
            count[ch] -= 1
    
    for value in count.values() :
        if abs(value) > 3 :
            return False
    return True
print(checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab"))