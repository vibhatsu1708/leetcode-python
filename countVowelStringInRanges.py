# Count Vowel Strings in Ranges
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

def vowelStrings (words, queries) :
    vowels = set("aeiou")
    length = len(words)
    prefix = [0] * (length+1)
    for i in range (length) :
        prefix[i+1] = prefix[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
    result = []
    for query in queries :
        result.append(prefix[query[1]+1] - prefix[query[0]])
    return result
print(vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))