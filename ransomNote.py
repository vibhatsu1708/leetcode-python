# Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct (ransomNote, magazine) :
    equalCount = {}
    for ch in magazine :
        if ch not in equalCount :
            equalCount[ch] = 1
        else :
            equalCount[ch] += 1
    for ch in ransomNote :
        if ch not in equalCount or equalCount[ch] == 0 :
            return False
        equalCount[ch] -= 1
    return True
print(canConstruct(ransomNote = "aa", magazine = "aab"))