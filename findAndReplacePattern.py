# Find and Replace Pattern
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

def findAndReplacePattern (words, pattern) :
    trueWords = []
    for word in words :
        wordMap, patternMap = {}, {}
        isMatch = True
        for i in range (len(word)) :
            wCh, pCh = word[i], pattern[i]
            if (wCh in wordMap and wordMap[wCh] != pCh) or (pCh in patternMap and patternMap[pCh] != wCh) : 
                isMatch = False
                break
            wordMap[wCh] = pCh
            patternMap[pCh] = wCh
        if isMatch:
            trueWords.append(word)
    return trueWords
print(findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
