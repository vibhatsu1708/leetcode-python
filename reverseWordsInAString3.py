# Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords (s) :
    s = s[::-1]
    s = s.split(" ")
    left, right = 0, len(s)-1
    while (left < right) :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return " ".join(s)
print(reverseWords(s = "Let's take LeetCode contest"))