# Reverse Only Letters
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

def reverseOnlyLetters (s) :
    reverseS = ""
    for i in range (len(s)) :
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) :
            reverseS += s[i]
    reverseS = reverseS[::-1]
    newS = []
    for i in range (len(reverseS)) :
        newS.append(reverseS[i])
    for i in range (len(s)) :
        if s[i].isalpha() == False :
            newS.insert(i, s[i])
    return s, reverseS, "".join(newS)
print(reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))