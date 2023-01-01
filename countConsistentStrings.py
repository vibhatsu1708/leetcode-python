# Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

def countConsistentStrings (allowed, words) :
    count = 0
    for word in words :
        consistent = True
        for i in word :
            if i not in allowed :
                consistent = False
                break
        if consistent :
            count += 1
    return count
    
print(countConsistentStrings(allowed="cad", words=["cc","acd","b","ba","bac","bad","ac","d"]))