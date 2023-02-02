# Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern (pattern, s) :
    sWords = s.split(" ")
    if len(pattern) != len(sWords) :
        return False
    patternMap, sWordsMap = {}, {}
    for i in range (len(pattern)) :
        patternCh, sWord = pattern[i], sWords[i]
        if (patternCh in patternMap and patternMap[patternCh] != sWord) or (sWord in sWordsMap and sWordsMap[sWord] != patternCh) :
            return False
        patternMap[patternCh] = sWord
        sWordsMap[sWord] = patternCh
    return True
print(wordPattern(pattern = "aaa", s = "aa aa aa aa"))