# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    commonPre = ""
    for i in range(len(strs[0])):
        for str in strs:
            if i == len(str) or str[i] != strs[0][i]:
                return commonPre
        commonPre += str[i]
    return commonPre
print(longestCommonPrefix(strs = ["ab", "a"]))

