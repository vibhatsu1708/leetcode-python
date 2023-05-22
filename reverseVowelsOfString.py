# Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverseVowels (s) :
    s = list(s)
    left, right = 0, len(s)-1
    vowels = "aeiou"
    while (left < right):
        if s[left] not in vowels and s[right] in vowels:
            left += 1
        if s[left] in vowels and s[right] not in vowels:
            right -= 1
        if s[left] not in vowels and s[right] not in vowels:
            left += 1
            right -= 1
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)
print(reverseVowels(s = "leetcode"))
