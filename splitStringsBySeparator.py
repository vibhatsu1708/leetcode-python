# Split Strings by Separator
# Given an array of strings words and a character separator, split each string in words by separator.

# Return an array of strings containing the new strings formed after the splits, excluding empty strings.

# Notes

# separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
# A split may result in more than two strings.
# The resulting strings must maintain the same order as they were initially given.

def splitWordsBySeparator(words, separator):
    result = []
    for string in words:
        left, right = 0, 0
        while right < len(string):
            if string[right] == separator:
                if left != right:
                    result.append(string[left:right])
                left = right + 1
            right += 1
        if left != right:
            result.append(string[left:right])
    return result
print(splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))