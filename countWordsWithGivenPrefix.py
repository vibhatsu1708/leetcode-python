# Counting Words With a Given Prefix
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

def prefixCount (words, pref) :
    count = 0
    for word in words :
        if word[0:len(pref)] == pref :
            count += 1
    return count
print(prefixCount(words=["leetcode","win","loops","success"], pref="code"))