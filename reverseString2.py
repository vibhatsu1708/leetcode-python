# Reverse String II
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

def reverseStr (s, k) :
    # incorrect approach
    # i = 0
    # while (i < len(s)) :
    #     if (i+k) > len(s) :
    #         break
    #     substr = s[i:i + k]
    #     s = s[:i] + substr[::-1] + s[i+k:]
    #     i += 2*k
    # return s
            
    # correct approach
    sList = list(s)
    for i in range (0, len(sList), 2*k) :
        sList[i:i+k] = (sList[i:i+k])[::-1]
    return "".join(sList)
print(reverseStr(s = "abcdefg", k = 2))