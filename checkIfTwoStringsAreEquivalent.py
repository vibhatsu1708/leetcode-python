# Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

def arrayStringsAreEqual (word1, word2) :
    strWord1 = ""
    strWord2 = ""
    for i in word1 :
        for j in i :
            strWord1 += j
    for i in word2 :
        for j in i :
            strWord2 += j
    if strWord1 == strWord2 :
        return True
    else :
        return False
print(arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))