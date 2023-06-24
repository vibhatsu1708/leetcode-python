# Find Maximum Number of String Pairs
# You are given a 0-indexed array words consisting of distinct strings.

# The string words[i] can be paired with the string words[j] if:

# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.

# Note that each string can belong in at most one pair.

def maximumNumberOfStringPairs(words):
    count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[j][::-1] == words[i]:
                count += 1
    return count
print(maximumNumberOfStringPairs( words = ["aa","ab"]))