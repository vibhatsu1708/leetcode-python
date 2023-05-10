# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
    anagramCount = {}
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in anagramCount:
            anagramCount[sortedWord] = []
        anagramCount[sortedWord].append(word)
    return list(anagramCount.values())
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))