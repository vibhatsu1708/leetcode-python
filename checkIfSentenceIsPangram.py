# Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram (sentence) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet :
        if ch not in sentence.lower() :
            return False
    return True
    
print(checkIfPangram(sentence="leetcode"))

# testcase 1: "thequickbrownfoxjumpsoverthelazydog" should return true, the sentence contains every letter of the english alphabet.
# testcase 1: ""leetcode"" should return false, the sentence doesn't contain every letter of the english alphabet.