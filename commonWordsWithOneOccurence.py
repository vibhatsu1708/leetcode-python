# Count Common Words With One Occurrence
# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

def countWords (words1, words2) :
    # custom functions to avoid repetition of code.
    def countWords (words) :
        seen = {}
        for word in words :
            if word not in seen :
                seen[word] = 1
            else :
                seen[word] += 1
        return seen
    def removeMultipleOccurrences (wordsCount) :
        for value in list(wordsCount.keys()) :
            if wordsCount[value] > 1 :
                del wordsCount[value]
        return wordsCount
    
    # instances of the function.
    words1Count = countWords(words1)
    words2Count = countWords(words2)
    newWords1Count = removeMultipleOccurrences(words1Count)
    newWords2Count = removeMultipleOccurrences(words2Count)
    
    # count variable set to 0.
    count = 0
    
    # checks if the word in newWords1Count exists in newWords2Count or not.
    for word in list(newWords1Count) :
        if word in list(newWords2Count) :
            count += 1
    return count

print(countWords(words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]))