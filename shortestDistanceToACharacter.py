# Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers
# answers where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of
# character c in s. The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

def shortestToChar(s, c):
    indices = []
    for i in range(len(s)):
        if s[i] == c:
            indices.append(i)
    result = []
    for i in range(len(s)):
        shortestDist = float("inf")
        for j in indices:
            dist = abs(i-j)
            shortestDist = min(dist, shortestDist)
        result.append(shortestDist)
    return result



print(shortestToChar(s = "aaab", c = "b"))
