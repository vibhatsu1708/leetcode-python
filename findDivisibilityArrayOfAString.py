# Find the Divisibility Array of a String
# You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.
# The divisibility array div of word is an integer array of length n such that:
# div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
# div[i] = 0 otherwise.
# Return the divisibility array of word.

def divisibilityArray (word, m) :
    result = []
    value = 0
    for i in range (len(word)) :
        value = (value*10 + int(word[i]))%m
        result.append(int(value == 0))
    return result
print(divisibilityArray(word = "998244353", m = 3))