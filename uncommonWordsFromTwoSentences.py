# Uncommon Words from Two Sentences
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

def uncommonFromSentences (s1, s2) :
    uncommon, count = [], {}
    s1 += " " + s2
    for i in s1.split(" ") :
        if i in count :
            count[i] += 1
        else :
            count[i] = 1
    for i, key in enumerate (count) :
        if count[key] == 1 :
            uncommon.append(key)
    return uncommon
print(uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour"))