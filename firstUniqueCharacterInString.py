# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar (s) :
    seen = {}
    character = ""
    for i in range (len(s)) :
        if s[i] not in seen :
            seen[s[i]] = 1
        else :
            seen[s[i]] += 1
    for i, value in enumerate (seen) :
        if seen[value] == 1 :
            character = value
            break
    for i in range (len(s)) :
        if s[i] == character :
            return i
    return -1
print(firstUniqChar(s="aabb"))