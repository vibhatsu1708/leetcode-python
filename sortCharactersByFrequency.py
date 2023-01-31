# Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

def frequencySort (s) :
    sortedS = []
    count = {}
    for i in range (len(s)) :
        if s[i] not in count :
            count[s[i]] = 1
        else :
            count[s[i]] += 1
    sortedCountByFrequency = dict(sorted(count.items(), key = lambda freq : freq[1], reverse=True))
    sortedChars = ""
    for i, value in enumerate(sortedCountByFrequency) :
        sortedChars += (value*sortedCountByFrequency[value])
    return sortedChars
print(frequencySort(s = "cccaaa"))