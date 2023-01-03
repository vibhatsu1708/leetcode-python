# Check if All Characters Have Equal Number of Occurrences
# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

def areOccurrencesEqual (s) :
    counts = {}
    for i in range (len(s)) :
        if s[i] not in counts :
            counts[s[i]] = 1
        else :
            counts[s[i]] += 1    
    baseValue = list(counts.values())[0]
    flag = True
    for value in counts.values() :
        if baseValue != value :
            flag = False
            break
    return flag
        
print(areOccurrencesEqual(s="tveixwaeoezcf")) 