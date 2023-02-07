# Vowels of All Substrings
# Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.
# A substring is a contiguous (non-empty) sequence of characters within a string.
# Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.

def countVowels (word) :
    # vowels = "aeiou"
    # count = 0
    # for i in range (0, len(word)) :
    #     for j in range (0, len(word)) :
    #         if (word[i:j+1] != "") :
    #             for k in word[i:j+1] :
    #                 if k in vowels :
    #                     count += 1
    # return count
    
    count = 0
    vowels = "aeiou"
    for i in range (len(word)) :
        substr = word[i]
        if substr in vowels :
            count += ((len(word)-i) * (i + 1))
    return count
print(countVowels(word = "abc"))