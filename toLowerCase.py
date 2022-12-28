# To Lower Case
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

def toLowerCase (s) :
    newstr = ""
    for ch in s :
        if ord(ch) >= 65 and ord(ch) <= 90 :
            newstr += chr(ord(ch) + 32)
        else :
            newstr += ch
    return newstr
print(toLowerCase(s="LOVELY"))