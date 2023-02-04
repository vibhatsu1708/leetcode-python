# Append Characters to String to Make Subsequence
# You are given two strings s and t consisting of only lowercase English letters.
# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

def appendCharacters (s, t) :
    # pointer = 0
    # for ch in s :
    #     if ch == t[pointer] :
    #         pointer += 1
    #         if pointer == len(t) :
    #             return 0
    # return len(t) - pointer
    
    first, second = 0, 0
    while (first < len(s) and second < len(t)) :
        if s[first] == t[second] :
            first += 1
            second += 1
        else :
            first += 1
    return len(t) - second
print(appendCharacters(s = "coaching", t = "coding"))