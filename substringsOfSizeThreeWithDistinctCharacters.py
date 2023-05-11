# Substrings of Size Three with Distinct Characters
# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

def countGoodSubstrings (s) :
    k = 3
    count = 0
    for i in range(len(s) - (k-1)):
        if len("".join(sorted(set(s[i:i+k])))) == 3:
            count += 1
    return countg
print(countGoodSubstrings(s = "aababcabc"))