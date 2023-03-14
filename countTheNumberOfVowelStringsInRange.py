# Count the Number of Vowel Strings in Range
# You are given a 0-indexed array of string words and two integers left and right.
# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

def vowelStrings (words, left, right) :
    count = 0
    def isVowel (ch) :
        vowels = "aeiouAEIOU"
        if ch in vowels :
            return True
        return False
        
    for word in range (left, right+1) :
        if isVowel(words[word][0]) and isVowel(words[word][-1]) :
            count += 1
        continue
    return count
print(vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))